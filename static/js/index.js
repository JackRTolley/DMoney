'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var App = function (_React$Component) {
    _inherits(App, _React$Component);

    function App() {
        _classCallCheck(this, App);

        return _possibleConstructorReturn(this, (App.__proto__ || Object.getPrototypeOf(App)).apply(this, arguments));
    }

    _createClass(App, [{
        key: "render",
        value: function render() {
            return React.createElement(
                "div",
                null,
                React.createElement(Header, null),
                React.createElement(Sidebar, null),
                React.createElement(ProjectView, null)
            );
        }
    }]);

    return App;
}(React.Component);

var Header = function (_React$Component2) {
    _inherits(Header, _React$Component2);

    function Header() {
        _classCallCheck(this, Header);

        return _possibleConstructorReturn(this, (Header.__proto__ || Object.getPrototypeOf(Header)).apply(this, arguments));
    }

    _createClass(Header, [{
        key: "render",
        value: function render() {
            return React.createElement(
                "header",
                null,
                "MR LOCAL MONEYBAGS"
            );
        }
    }]);

    return Header;
}(React.Component);

var Sidebar = function (_React$Component3) {
    _inherits(Sidebar, _React$Component3);

    function Sidebar() {
        _classCallCheck(this, Sidebar);

        return _possibleConstructorReturn(this, (Sidebar.__proto__ || Object.getPrototypeOf(Sidebar)).apply(this, arguments));
    }

    _createClass(Sidebar, [{
        key: "render",
        value: function render() {
            return React.createElement(
                "div",
                null,
                "this is a side bar"
            );
        }
    }]);

    return Sidebar;
}(React.Component);

var ProjectView = function (_React$Component4) {
    _inherits(ProjectView, _React$Component4);

    function ProjectView() {
        _classCallCheck(this, ProjectView);

        return _possibleConstructorReturn(this, (ProjectView.__proto__ || Object.getPrototypeOf(ProjectView)).apply(this, arguments));
    }

    _createClass(ProjectView, [{
        key: "render",
        value: function render() {
            return React.createElement(
                "div",
                { "class": "list-group list-group-flush" },
                this.props.children
            );
        }
    }]);

    return ProjectView;
}(React.Component);

var Project = function (_React$Component5) {
    _inherits(Project, _React$Component5);

    function Project() {
        _classCallCheck(this, Project);

        return _possibleConstructorReturn(this, (Project.__proto__ || Object.getPrototypeOf(Project)).apply(this, arguments));
    }

    _createClass(Project, [{
        key: "render",
        value: function render() {
            return React.createElement(
                "div",
                { className: "card" },
                React.createElement(
                    "div",
                    { className: "card-body" },
                    React.createElement(
                        "h5",
                        { className: "card-title" },
                        this.props.name
                    ),
                    React.createElement(
                        "p",
                        { className: "card-text" },
                        "Default card text"
                    ),
                    React.createElement(
                        "div",
                        { className: "row" },
                        React.createElement(
                            "button",
                            { className: "btn btn-secondary" },
                            React.createElement("i", { className: "fas fa-angle-double-up fa-lg" })
                        ),
                        React.createElement(
                            "button",
                            { className: "btn btn-primary" },
                            "More Info"
                        ),
                        React.createElement(
                            "button",
                            { className: "btn btn-secondary" },
                            React.createElement("i", { className: "fas fa-chevron-down" })
                        )
                    )
                )
            );
        }
    }]);

    return Project;
}(React.Component);

var UserView = function (_React$Component6) {
    _inherits(UserView, _React$Component6);

    function UserView() {
        _classCallCheck(this, UserView);

        return _possibleConstructorReturn(this, (UserView.__proto__ || Object.getPrototypeOf(UserView)).apply(this, arguments));
    }

    _createClass(UserView, [{
        key: "render",
        value: function render() {
            return React.createElement(
                "div",
                { className: "col" },
                React.createElement(
                    "div",
                    { className: "col" },
                    React.createElement("i", { "class": "fas fa-wallet fa-7x" }),
                    React.createElement(
                        "p",
                        null,
                        "My Account"
                    )
                ),
                React.createElement(
                    "div",
                    { className: "col" },
                    React.createElement("i", { "class": "fas fa-hammer fa-7x" }),
                    React.createElement(
                        "p",
                        null,
                        "My Projects"
                    )
                ),
                React.createElement(
                    "div",
                    { className: "col" },
                    React.createElement("i", { "class": "fas fa-comment-dollar fa-7x" }),
                    React.createElement(
                        "p",
                        null,
                        "My Investments"
                    )
                )
            );
        }
    }]);

    return UserView;
}(React.Component);

document.querySelectorAll('.project').forEach(function (domContainer) {
    // Read the comment ID from a data-* attribute.
    var commentID = parseInt(domContainer.dataset.commentid, 10);
    console.log(domContainer);
    ReactDOM.render(React.createElement(Project, domContainer.dataset), domContainer);
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