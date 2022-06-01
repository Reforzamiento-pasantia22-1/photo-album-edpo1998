import md5 from 'md5';


// Modulo a utilizar para extraer la imagen del perfil
const gravatar = (email) => {
  const base = 'https://gravatar.com/avatar/';
  const formattedEmail = (email).trim().toLowerCase();
  const hash = md5(formattedEmail, { encoding: "binary" });
  return `${base}${hash}`
};

export default gravatar;