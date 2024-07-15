import axios from "axios";
import router from "@/router/.";
import { CustomError } from "./errorUtils";

export function getToken() {
  return localStorage.getItem("token");
}

export function logout() {
  localStorage.removeItem("token");
  console.log("User token is being deleted");
  router.push("/");
}

export async function checkAuth() {
  const token = getToken();
  try {
    const authResponse = await axios.post(
      "https://ao9ww2ed5d.execute-api.us-east-1.amazonaws.com/dev/auth",
      {
        token: token,
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

export async function signup(uid, pass) {
  try {
    const signupResponse = await axios.post(
      "https://ao9ww2ed5d.execute-api.us-east-1.amazonaws.com/dev/auth/register",
      {
        user_id: uid,
        password: pass,
      }
    );
    console.log("Signup successful, redirecting to login");
    login(uid, pass);
  } catch (error) {
    console.error("Signup failed:", error);
  }
}

export async function login(uid, pass) {
  try {
    const loginResponse = await axios.post(
      "https://ao9ww2ed5d.execute-api.us-east-1.amazonaws.com/dev/auth/login",
      {
        user_id: uid,
        password: pass,
      }
    );
    const formattedResponse = {
      statusCode: loginResponse.data.statusCode,
      body: loginResponse.data.body,
    };
    switch (formattedResponse.statusCode) {
      default:
        throw CustomError.fromJSON(formattedResponse);
      case 200:
        saveToken(loginResponse);
        router.push("/drive");
        break;
    }
  } catch (error) {
    // alert(error.body);
    throw error;
  }
  console.log("finished");
}
