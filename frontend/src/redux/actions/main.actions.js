
import { action } from "../const/const.redux";


export const modalImage = payload => ({
    type: action.INSERT_IMAGE,
    payload,
});

export const modalSession = payload => ({
    type: action.MODAL_SESSION,
    payload,
});

export const loginRequest = payload => ({
    type: action.LOGIN_REQUEST,
    payload,
});
  
export const logoutRequest = payload => ({
    type: action.LOGOUT_REQUEST,
    payload,
});
  
export const registerRequest = payload => ({
    type: action.REGISTER_REQUEST,
    payload,
});


export const galleryRequest = payload => ({
    type: action.GALLERY_REQUEST,
    payload,
});


export const showAlbum = payload => ({
    type: action.SHOW_ALBUM,
    payload,
});


export const addImage = payload => ({
    type: action.ADD_IMAGE,
    payload,
})

