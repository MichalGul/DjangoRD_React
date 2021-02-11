import React from "react";
import {AppBar, Toolbar, Typography, CssBaseline, makeStyles, Grid} from "@material-ui/core";


//Create custom style for material UI
const useStyle = makeStyles((theme) => ({ //ovveride css of some class
    appBar: {
        borderBottom: `1px solid ${theme.palette.divider}`,
    },
}))


function Header() {
    const classes = useStyle() // use custom CSS class

    return ( //Component render code !
        <React.Fragment>
            <CssBaseline />
            <AppBar //NAVBAR JAK W BOOTSTRAPIE
                position="static"
                color="white"
                elevation={0}
                className={classes.appBar}
            >
                <Toolbar>
                    <Grid container spacing={2}>
                        <Grid item xs={1}>
                            <Typography variant='h6' color="inherit" noWrap>
                                BlogmeUp
                            </Typography>
                        </Grid>
                        <Grid item xs={1}>
                            <Typography variant='h6' color="inherit" noWrap>
                                BlogmeDown
                            </Typography>
                        </Grid>
                    </Grid>
                </Toolbar>
            </AppBar>

        </React.Fragment>
    )
}

export default Header;
