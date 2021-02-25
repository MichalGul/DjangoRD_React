import React from "react";
import {AppBar, Toolbar, Typography, CssBaseline, makeStyles, Grid, Link, Button} from "@material-ui/core";
import { NavLink } from 'react-router-dom';

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
                            <Typography
                                variant='h6'
                                color="inherit"
                                noWrap
                                className={classes.toolbarTitle}>
                                <Link
                                    component={NavLink}
                                    to="/"
                                    underline="none"
                                    color="textPrimary">
                                    BlogmeUp

                                </Link>
                            </Typography>
                        </Grid>
                        <Grid item xs={1}>
                        <nav>
                            <Typography variant='h6' color="inherit" noWrap>
                                <Link
                                    color="textPrimary"
                                    href="#"
                                    className={classes.link}
                                    component={NavLink}
                                    to="/register">

                                    Register
                                </Link>
                            </Typography>
                        </nav>
                        </Grid>
                        <Grid item xs={1}>
                            <Button
                                href="#"
                                color="primary"
                                variant="outlined"
                                className={classes.link}
                                component={NavLink}
                                to="/login"
                            >
                                Login
                            </Button>
                        </Grid>
                        <Grid item xs={1}>
                            <Button
                                href="#"
                                color="primary"
                                variant="outlined"
                                className={classes.link}
                                component={NavLink}
                                to="/logout"
                            >
                            Logout
                        </Button>
                        </Grid>
                    </Grid>
                </Toolbar>
            </AppBar>

        </React.Fragment>
    )
}

export default Header;
