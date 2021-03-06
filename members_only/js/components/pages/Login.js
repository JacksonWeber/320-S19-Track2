import React, {Component} from 'react';
import { Route, Redirect} from 'react-router'
import Cookies from 'universal-cookie';
import Notification from "../Notification";


class Login extends Component {

    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);

        const cookies = new Cookies();
        let token = cookies.get('user_token');

        if (token == null) {
            this.state = {
                logged_in: false,
                notificationText: '',
                verRequestComplete: false,
                needsVerification: false,
            }
        } else {
            this.state = {
                logged_in: true,
                notificationText: '',
                verRequestComplete: true,
                needsVerification: false,
            }
        }
    }

    checkIsVerified(token) {
        let xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        this.props.updateToken(token);

        xhr.open("GET", "/api/user/current_user/");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.setRequestHeader("cache-control", "no-cache");
        xhr.setRequestHeader("Authorization", "Token " + token);

        xhr.addEventListener("readystatechange", event => {
            if (event.target.readyState === 4) {
                let response_data = JSON.parse(event.target.responseText);

                
                if(response_data.is_verified){                  
                    this.setState({
                        verRequestComplete: true,
                        needsVerification: false,
                    });
                }else{
                    this.setState({
                        verRequestComplete: true,
                        needsVerification: true,
                    });
                }
            }
          });

        xhr.send();
    }

    handleSubmit(event) {
        let data = JSON.stringify({
            "username": this.email.value,
            "password": this.password.value,
        });

        let xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener("readystatechange", (event) => {
          if (event.target.readyState === 4) {
              let response_data = JSON.parse(event.target.responseText);

              if (typeof response_data.token === 'undefined') {
                  this.setState({
                      notificationText: 'Incorrect Credentials.',
                      notificationType: 'danger'
                  });

                  return;
              }

              console.log(response_data);
              const cookies = new Cookies();
              cookies.set('user_token', response_data.token, {path: "/"});

              this.checkIsVerified(response_data.token)

              this.setState({
                logged_in: true
            });
              
          }
        });

        xhr.open("POST", "/api-token-auth/");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.setRequestHeader("cache-control", "no-cache");

        xhr.send(data);

        event.preventDefault();
    }

    render() {

        if(this.state.logged_in && this.state.verRequestComplete){
            if(this.state.needsVerification){
                return (<Redirect to="/user/verification"/>)
            }else{
                return (<Redirect to="/homefeed"/>)
            }
        }else{
            return(
                <form onSubmit={this.handleSubmit}>
                <div className="columns">
                    <div className="column is-offset-one-quarter is-half">
                        <h1 className="title" style={header}>Login</h1>

                        <Notification text={this.state.notificationText} type={this.state.notificationType} />

                        <div className="field">
                            <p className="control has-icons-left has-icons-right">
                                <input className="input" type="email" placeholder="Email"
                                       ref={(input) => this.email = input}/>
                                <span className="icon is-small is-left">
                          <i className="fas fa-envelope"></i>
                        </span>
                            </p>
                        </div>
                        <div className="field">
                            <p className="control has-icons-left">
                                <input className="input" type="password" placeholder="Password"
                                       ref={(input) => this.password = input}/>
                                <span className="icon is-small is-left">
                          <i className="fas fa-lock"></i>
                        </span>
                            </p>
                        </div>
                        <div className="field">
                            <p className="control">
                                <input type="submit" value="Login" className="button is-success"/>
                            </p>
                        </div>
                    </div>
                </div>
            </form>
            );
        }
    }
}

const header = {
    marginTop: '40px',
    fontVariant: 'small-caps',
    fontSize: '40px'
};

export default Login;
