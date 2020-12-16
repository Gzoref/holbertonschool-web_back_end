import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser(uploadPhoto, createUser) {
  try {
    const photo = await uploadPhoto();
    const user = await createUser();

    return Promise.resolve({photo, user,});
  } catch (error) {
    return Promise.resolve({ photo: null, user: null });
  }
}
