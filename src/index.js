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
        <div class="list-group list-group-flush">
            {this.props.children}
        </div>
        )
    }
}

class Project extends React.Component{
    render(){
        return (
            <div className="card">
                <div className="card-body">
                    <h5 className="card-title">{this.props.name}</h5>
                    <p className="card-text">Default card text</p>
                    <div className="row">
                    
                    <button className="btn btn-secondary">
                    <i className="fas fa-angle-double-up fa-lg"></i>
                    </button>
                    
                    <button className="btn btn-primary">More Info</button>
                    
                    <button className="btn btn-secondary">
                    <i className="fas fa-chevron-down"></i>
                    </button>
                    
                    </div>
                </div>
            </div>
        )
    }
}

class UserView extends React.Component{
    render(){
        return (
            <div className="col">
                <div className="col">
                    <i class="fas fa-wallet fa-7x"></i>
                    <p>My Account</p>
                </div>
                <div className="col">
                    <i class="fas fa-hammer fa-7x"></i>
                    <p>My Projects</p>
                </div>
                <div className="col">
                    <i class="fas fa-comment-dollar fa-7x"></i>
                    <p>My Investments</p>
                </div>
            </div>
        )
    }
}
document.querySelectorAll('.project')
  .forEach(domContainer => {
    // Read the comment ID from a data-* attribute.
    const commentID = parseInt(domContainer.dataset.commentid, 10);
    console.log(domContainer);
    ReactDOM.render(   <Project {...(domContainer.dataset)}/>,
    domContainer
    );
});

/*
ReactDOM.render(
    <UserView />,
    document.querySelector('#userView')
);
/*
/*

ReactDOM.render(
    <Header />,
    document.querySelector('#header')
);

ReactDOM.render(
    <ProjectView />,
    document.querySelector('#projectView')
)
*/