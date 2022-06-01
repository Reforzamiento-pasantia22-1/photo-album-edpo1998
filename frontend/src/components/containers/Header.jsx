// React
import { Link } from 'react-router-dom';
// Redux
import { connect } from 'react-redux';
import {logoutRequest,modalSession} from '../../redux/actions/main.actions.js'
// Utils
import classNames from 'classnames';
import gravatar from '../../utils/gravatar.js';
// Images
import userIcon from '../../public/assets/images/user-icon.png';
// Styles
import "../../public/assets/css/components/Header.scss"

function Header(props) {

  const { user, isLogin, isRegister } = props;
  
  const hasUser = Object.keys(user).length > 0;

  const headerClass = classNames('header', {
    isLogin,
    isRegister,
  });

  const handleLogout = () => {
    props.logoutRequest({});
  }
  
  const showLogin =() => { 
    const newLocal = true;
    props.modalSession(newLocal)

  }

  return (
    <header className={headerClass}>
      <div className="header__menu">
        <div className="header__menu--profile">
          {hasUser ?
            <img src={gravatar(user.email)} alt={user.email} /> :
            <img src={userIcon} alt="" />
          }
          {hasUser ?
            <p>{user.name}</p> 
            : <p>Perfil</p>
          }
          
        </div>
        <ul>
          
          {hasUser ? 
            <>
              <li><a href="/" onClick={handleLogout}>Cerrar Sesión</a></li>
              <li><a href="/" onClick={handleLogout}>Crear Album</a></li>
              <li><a href="/" onClick={handleLogout}>Crear Imagen</a></li>
            </>
            
            :
            <li>
              <Link to="/" onClick={showLogin}>
                Iniciar sesión
              </Link>
            </li>
          }
        </ul>
      </div>
    </header>
  );
}

const mapStateToProps = state => {
  return {
    user: state.user,
    mlogin: state.mlogin,
  };
};

const mapDispatchToProps = {
  logoutRequest,
  modalSession
}

export default connect(mapStateToProps, mapDispatchToProps)(Header);