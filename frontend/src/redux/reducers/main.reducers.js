
const initialState = {
  "user": {},
  "gallery": [],
  "album": [],
  "mlogin": false,
  "showAlbum":false,
  "mimage":false,
}

const reducer = (state = initialState, action) => {
    switch (action.type) {
      case 'SHOW_ALBUM':
          return {
            ...state,
            album: action.payload
      } 
      case 'GALLERY_REQUEST':
        return {
          ...state,
          gallery: action.payload,
        }
      case 'LOGIN_REQUEST':
        return {
          ...state,
          user: action.payload,
        }
      case 'LOGOUT_REQUEST':
        return {
          ...state,
          user: action.payload,
        }
      case action.REGISTER_REQUEST:
         return {
           ...state,
           user: action.payload
         }
      case 'MODAL_SESSION':
          return {
            ...state,
            mlogin: action.payload
         }    
      case 'ADD_IMAGE':
          return {
            ...state,
            album: action.payload
      }  
      case 'INSERT_IMAGE':
        return {
          ...state,
          mimage: action.payload
       } 
      default: 
        return state;
    }
    
  }
  
  export default reducer;