'use strict';

class App extends React.Component{
    render(){
        return (
            <div>
                <Header />
                <Sidebar />
                <ProjectView />
            </div>
        )
    }
}

class Header extends React.Component{
    render(){
        return (
        <header>
            MR LOCAL MONEYBAGS
        </header>
        )
    }
}

class Sidebar extends React.Component{

    render(){
        return (
        <div>
            this is a side bar
        </div>
        )
    }
}

class ProjectView extends React.Component{
    render(){
        return (
        <div>
            This is the project view
        </div>
        )
    }
}

class Project extends React.Component{
    render(){
        return (
            <div className="row">
                <div className="col-2">
                    <button>Upvote</button>
                    <p>{this.props.score}</p>
                    <button>Downvote</button>
                </div>
                <div className="col-8">
                    <p>{this.props.name}</p>
                </div>
                <div className="col-2">
                    <p>Money Bags</p>
                </div>
            </div>
        )
    }
}

class UserView extends React.Component{
    render(){
        return (
            <div className="col">
                <div className="row">
                    User Account
                </div>
                <div className="row">
                    My Projects
                </div>
                <div className="row">
                    My Investments 
                </div>
            </div>
        )
    }
}

document.querySelectorAll('.project')
  .forEach(domContainer => {
    // Read the comment ID from a data-* attribute.
    const commentID = parseInt(domContainer.dataset.commentid, 10);

    ReactDOM.render(   <Project {...(domContainer.dataset)}/>,
    domContainer
    );
});

ReactDOM.render(
    <UserView />,
    document.querySelector('#userView')
);

ReactDOM.render(
    <Header />,
    document.querySelector('#header')
);