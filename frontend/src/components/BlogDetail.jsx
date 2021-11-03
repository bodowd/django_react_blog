import axios from "axios";
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

const BlogDetail = (props) => {
  const [blog, setBlog] = useState({});

  useEffect(() => {
    const slug = props.match.params.id;

    const fetchData = async () => {
      try {
        const res = await axios.get(
          `${process.env.REACT_APP_API_URL}/api/blog/${slug}`
        );
        setBlog(res.data);
      } catch (err) {}
    };

    fetchData();
    // whenever the id in the url has a change, this hook will be triggered
  }, [props.match.params.id]);

  const createBlog = () => {
    return { __html: blog.content };
  };

  // capitalize the first letter because they are stored in DB in all lowercase
  const capitalizeFirstLetter = (word) => {
    if (word) {
      // capitalize index 0 and concatenate the rest of the string
      return word.charAt(0).toUpperCase() + word.slice(1);
    }
    return "";
  };

  return (
    <div className="container mt-3">
      <h1 className="display-2">{blog.title}</h1>
      <h2 className="text-muted mt-3">Category: {capitalizeFirstLetter(blog.category)}</h2>
      <h4>{blog.month} {blog.day}</h4>
      <div className="mt-5 mb-5" dangerouslySetInnerHTML={createBlog()} />
      <hr />
      <p className="lead mb-5">
        <Link to="/blog" className="font-weight-bold">
          Back to Blogs
        </Link>
      </p>
    </div>
  );
};

export default BlogDetail;
