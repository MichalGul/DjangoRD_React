import React from "react";
import {Typography, Container, makeStyles, Grid, Link, Box} from "@material-ui/core";

function PostLoading(Component) {
	return function PostLoadingComponent({isLoading, ...props}) {
		if(!isLoading) return <Component  {...props}/>; //if component is loaded => load Posts Component
		return (
			<p style={{fontSize: '25px'}}>
				We are waiting form the data to load! ...
			</p>
		);
	};
}

export default PostLoading;