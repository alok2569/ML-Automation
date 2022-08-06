import { Navigate, useRoutes } from 'react-router-dom';
import DashboardLayout from './Pages/DashboardLayout';
import Dashboard from './Pages/Dashboard';
import Test from './Pages/Test';

export default function Router(){
    return useRoutes([
        {
            path:'/',
            // element: <Navigate to="/Dashboard" replace />
            element: <DashboardLayout />,
            children: [
                { path:"", element: <Navigate to="/dashboard" replace /> },
                {
                    path:'dashboard',
                    element: <Dashboard />
                },
                {
                    path:'test',
                    element: <Test />
                }
            ]
        }
    ])
}