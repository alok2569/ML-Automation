import React, { useState, useEffect } from 'react';
import DOMParserReact, { parse } from 'dom-parser-react';
import sanitizeHtml from 'sanitize-html';
import { Button, Card, CardBody, CardTitle, CardSubtitle, Container,Row,Col, Badge, Form, FormGroup, FormText, Label, Input, ListGroup, ListGroupItem, Dropdown, DropdownItem, DropdownToggle, DropdownMenu } from 'reactstrap';
const axios = require('axios');

export default function Dashboard() {
    const [uploaded, setUploaded] = useState([]);
    const [refresh, setRefresh] = useState(false);
    const [tableHead, setTableHead] = useState();
    const [summary, setSummary] = useState();
    const [csvSelected, setCsvSelected] = useState();
    useEffect(() => {
        axios.get('http://localhost:8000/csv')
            .then((res) => {
                if (res.data) {
                    // let names = res.data
                    // console.log('resData', res.data)

                    const temp = res.data.map((item) => {
                        item.csv_file = item.csv_file.slice(19)
                        return item;
                    })
                    console.log('csv response: ', temp)
                    setUploaded(temp);
                }

            })
            .catch((err) => {
                console.log('Csv error: ', err)
            })
    }, [refresh])
    const formData = new FormData();
    const [csv, setCsv] = useState();
    const [dropOpen, setDropOpen] = useState(false);
    const handleCsvDrop=()=>{
        setDropOpen(!dropOpen);
    }
    const onButton = () => {
        const start = new Date(Date.now())
        formData.append('csv_file', csv);
        axios.post('http://localhost:8000/csv',
            formData,
            {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }
        )
            .then((data) => {
                console.log('Received: ', data);
                setRefresh(true);
                const end = new Date(Date.now())
                console.log('time required in ', end - start)
            })
            .catch((err) => {
                console.log('err:', err);
            })
    }
    const handleItemClick = (e, i) => {
        console.log("click", i);
        const start = new Date(Date.now())
        setCsvSelected(i);
        axios.get(`http://localhost:8000/csvDetails/${i.id}`)
            .then((res) => {
                if (res.data) {
                    // let names = res.data
                    console.log('resData', res.data)
                    // const doc = new DOMParser().parseFromString(res.data.head, "text/html");
                    // const htmlSections = doc.childNodes[0].childNodes[1].childNodes
                    // console.log(doc.childNodes[0].childNodes[1].childNodes)
                    // const sections = Object.keys(htmlSections).map((key, i) => {
                    //     const el = htmlSections[key];
                    //     const contents = [el.innerHTML];
                    //     return <div key={i}>{contents}</div>
                    // })
                    const sanitizeHead = sanitizeHtml(res.data.head,{ allowedTags: ['table', 'thead', 'tr', 'th', 'td'], }
                        );

                    setTableHead(sanitizeHead);
                    const sanitize = sanitizeHtml(res.data.summary);
                    setSummary(sanitize);
                    const end = new Date(Date.now())
                    console.log('time required in ', end - start)

                }

            })
            .catch((err) => {
                const end = new Date(Date.now())
                console.log('time required in ', end - start)
                console.log('Csv error: ', err)
            })
    }

    const fileChangeHandler = (file) => {
        if (!file) {
            setCsv('');
            return;
        }
        setCsv(file);
        console.log('CsvFIle:', typeof (file));
    }

    return (
        <Container>

            <Row className="d-flex">
                <Col xs="3" className="bg-light border">
                <div className="p-2 flex"><Card
                >
                    <CardBody>
                        <CardTitle tag="h5">
                            Upload File
                        </CardTitle>
                        

                        <Form>
                            <FormGroup>
                                {/* <Label for="exampleFile">
                                    File
                                </Label> */}
                                <Input
                                    id="exampleFile"
                                    name="file"
                                    type="file"
                                    onChange={(event) => { fileChangeHandler(event.target.files[0] || null) }}
                                />

                            </FormGroup>
                        </Form>
                        <Button color='primary' onClick={onButton}>
                            Upload
                        </Button>
                    </CardBody>
                </Card></div>
                <div className="p-2 flex"><Card
                >
                    <CardBody>
                        <CardTitle tag="h5">
                            Uploaded Files
                        </CardTitle>
                        {/* <ListGroup>
                            {
                                uploaded.map((item) => (
                                    <ListGroupItem action tag="button" onClick={(e) => handleItemClick(e, item)} key={item.id} href='#'>
                                        {item.csv_file}
                                    </ListGroupItem>
                                ))

                            }
                        </ListGroup> */}

                        <Dropdown isOpen={dropOpen} toggle={handleCsvDrop}>
                           {
                            csvSelected ?
                            <DropdownToggle caret>   
                             {csvSelected.csv_file}
                            </DropdownToggle>
                            :
                            <DropdownToggle caret>  
                            Select 
                            </DropdownToggle>
                            }
                            <DropdownMenu color='primary' container="body">
                            {
                                uploaded.map((item) => (
                                <DropdownItem onClick={(e) => handleItemClick(e, item)} key={item.id}>
                                {item.csv_file}
                                </DropdownItem>
                                ))
                            }
                               
                            </DropdownMenu>
                        </Dropdown>

                    </CardBody>
                </Card></div>


           
            </Col>
            <Col xs="9">
            <div className="w-100 m-3 p-2">
                <h5>Head</h5>
                {/* {
                tableHead && <DOMParserReact source={tableHead}   />
                } */}
                <div dangerouslySetInnerHTML={{__html:tableHead}} />
            </div>
            <div className="w-100 m-3 p-2">
            <h5>Summary</h5>
                {
                    // summary && <DOMParserReact source={summary}   />
                   
                }
                <div dangerouslySetInnerHTML={{__html:summary}} />
            </div>
            </Col>
            </Row>
        </Container>
    );
}