import logo from './logo.svg';
import './App.css';
import React, {Component, useEffect, useState} from "react";
import Posts from "./components/Posts";
import PostLoadingComponent from "./components/PostLoading";

// class ConnectionExample extends Component {
//   componentDidMount() {
//     const apiUrl = 'httpls://127.0.0.1:8000/api/';
//     fetch(apiUrl)
//         .then((response) => response.json())
//         .then((data) => console.log(data))
//   }
//   render() {
//     return (
//         <div>Example connection</div>
//     )
//   }
// }
// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }


function App() {
  const PostLoading = PostLoadingComponent(Posts);
  const [appState, setAppState] = useState({ //setup state
    loading: false,
    posts: null,
  });

  useEffect(() => { // Opis wykorzystania useEffect do API -> https://www.smashingmagazine.com/2020/06/rest-api-react-fetch-axios/
    setAppState({loading: true});
    const apiUrl = `http://127.0.0.1:8000/api/`; // call main endpoint for all posts
    fetch(apiUrl)
        .then((data) => data.json())
        .then((posts) => {
          setAppState({loading: false, posts: posts});
        });
  }, [setAppState]);
  return (
      <div className="App">
        <h1>Latest Posts</h1>
        <PostLoading isLoading={appState.loading} posts={appState.posts} />
      </div>
  );
}

export default App;
