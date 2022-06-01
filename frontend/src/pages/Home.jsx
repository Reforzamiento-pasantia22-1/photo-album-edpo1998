// React
import { connect } from "react-redux";
// Components
import Login from "../components/modals/Login";
import ShowAlbum from "../components/modals/ShowAlbum";
import Gallery from "../components/containers/Gallery";
// Styles
import "../public/assets/css/pages/Home.scss"

function Home(props) {
  
    return (
    <div className="Home">
      <Login></Login>
      {
        Object.keys(props.user).length>0?
        <Gallery></Gallery>:
        ""
      }
      <ShowAlbum></ShowAlbum>
    </div>
    );
  }

  const mapStateToProps = state => {
    return {
      user: state.user,
    };
    
};

export default connect(mapStateToProps, null)(Home);