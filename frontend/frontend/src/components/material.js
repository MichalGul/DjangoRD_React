import React from "react";
import "../index.css"
import {Button, Typography} from "@material-ui/core";
import { makeStyles } from "@material-ui/core";

const useStyles = makeStyles({
    helloThereStyle : {
        fontStyle: 'oblique',
        color: 'gray',
        fontSize:'30px'
    },
    buttonStyles: {
        color: 'green',
        border: 0
    }
});

export default function Material() {
    const classes = useStyles();

    return (
        <div className="App">
            <Typography
                className={classes.helloThereStyle}
                color="primary"
                variant='h3'>
                Hello there!
            </Typography>
            <Button
                className={classes.buttonStyles}
                variant='outlined'
                color="secondary"
                fullWidth>

                First button
            </Button>
        </div>
    );
}