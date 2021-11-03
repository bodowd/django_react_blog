import React from "react";
import { Link } from "react-router-dom";

const Home = () => (
  <div className="container">
    <div className="jumbotron mt-5">
      <h1 className="display-4">Welcome to my blog</h1>
      <p className="lead">
      Read some posts below if you're interested</p>
      <hr className="my-4" />
      <p>Click below to check out the blog</p>
      <Link className="btn btn-primary btn-lg" role="button" to="/blog">
          Read on
      </Link>
    </div>
  </div>
);

export default Home;
