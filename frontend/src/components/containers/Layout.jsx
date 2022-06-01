// React
import React from 'react';
import { Outlet } from "react-router-dom";
// Components
import Header from './Header';
// Styles
import "../../public/assets/css/App.scss"
import 'bootstrap/dist/css/bootstrap.css';

const Layout = () => (
  <div className="App">
    <Header></Header>
    <Outlet />
  </div>
);

export default Layout;