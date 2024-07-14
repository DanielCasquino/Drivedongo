import axios from "axios";
import router from "@/router/.";

export function getToken() {
  return localStorage.getItem("token");
}

export function logout() {
  localStorage.removeItem("token");
  console.log("User token is being deleted");
  router.push("/");
}

export async function checkAuth() {
  const tok = getToken();
  try {
    const authResponse = await axios.post(
      "https://ao9ww2ed5d.execute-api.us-east-1.amazonaws.com/dev/auth",
      {
        "token": tok
      },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    switch (authResponse.data.statusCode) {
      case 404:
        throw new Error(authResponse.data.body);
      case 403:
        throw new Error(authResponse.data.body);
      case 200:
        console.log("User token is valid");
        return true;
    }
  } catch (error) {
    console.log(error);
    logout();
    return false;
  }
}

export function saveToken(response) {
  localStorage.setItem("token", response.data.token);
}
