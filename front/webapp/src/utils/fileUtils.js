import axios from "axios";
import { CustomError } from "./errorUtils";
import { checkAuth } from "./authUtils";
import { useNotificationStore } from "@/stores/notification-store";
import { useFileStore } from "@/stores/file-store";

export async function sendFile(metadata, b64) {
  const notiStore = useNotificationStore();
  try {
    const uid = await checkAuth();
    const uploadResponse = await axios.post(
      "https://ao9ww2ed5d.execute-api.us-east-1.amazonaws.com/dev/file/upload",
      {
        user_id: uid,
        file_name: metadata.name,
        file_content: b64,
      },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    const formattedResponse = {
      statusCode: uploadResponse.data.statusCode,
      body: uploadResponse.data.body,
    };

    switch (formattedResponse.statusCode) {
      case 201:
        notiStore.show(formattedResponse.statusCode, formattedResponse.body);
        break;
      default:
        throw CustomError.fromJSON(formattedResponse);
    }
  } catch (e) {
    notiStore.show(e.statusCode, e.body);
  }
}

export async function listFiles() {
  const notiStore = useNotificationStore();
  try {
    const uid = await checkAuth();
    const listResponse = await axios.post(
      "https://ao9ww2ed5d.execute-api.us-east-1.amazonaws.com/dev/file/list",
      {
        user_id: uid,
      }
    );
    const formattedResponse = {
      statusCode: listResponse.data.statusCode,
      body: listResponse.data.body,
      payload: listResponse.data.payload,
    };
    switch (formattedResponse.statusCode) {
      case 200:
        return formattedResponse.payload;
      default:
        throw CustomError.fromJSON(formattedResponse);
    }
  } catch (e) {
    notiStore.show(e.statusCode, e.body);
  }
}

export async function deleteFile(fileName) {
  console.log(fileName);
  const notiStore = useNotificationStore();
  try {
    const uid = await checkAuth();
    const deleteResponse = await axios.delete(
      "https://ao9ww2ed5d.execute-api.us-east-1.amazonaws.com/dev/file/delete",
      {
        user_id: uid,
        file_name: fileName,
      }
    );
    const formattedResponse = {
      statusCode: deleteResponse.data.statusCode,
      body: deleteResponse.data.body,
      payload: deleteResponse.data.payload,
    };
    console.log(deleteResponse);
    switch (formattedResponse.statusCode) {
      case 200:
        console.log("Reached 200");
        notiStore.show(formattedResponse.statusCode, formattedResponse.body);
        return formattedResponse.payload;
      default:
        throw CustomError.fromJSON(formattedResponse);
    }
  } catch (e) {
    notiStore.show(e.statusCode, e.body);
  }
}

export async function downloadFile(fileName) {
  const notiStore = useNotificationStore();
  try {
    const uid = await checkAuth();
    const response = await axios.post(
      "https://ao9ww2ed5d.execute-api.us-east-1.amazonaws.com/dev/file/download",
      {
        user_id: uid,
        file_name: fileName,
      }
    );
    const formattedResponse = {
      statusCode: response.data.statusCode,
      body: response.data.body,
      payload: response.data.payload,
    };
    console.log(formattedResponse);
    switch (formattedResponse.statusCode) {
      case 200:
        notiStore.show(formattedResponse.statusCode, formattedResponse.body);
        return formattedResponse.payload;
      default:
        throw CustomError.fromJSON(formattedResponse);
    }
  } catch (e) {
    notiStore.show(e.statusCode, e.body);
  }
}

export function base64ToFile(base64, filename, mimeType) {
  // Ensure the base64 string has no data URL prefix
  if (base64.startsWith("data:")) {
    base64 = base64.split(",")[1];
  }

  try {
    const byteString = atob(base64);
    const ab = new ArrayBuffer(byteString.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i++) {
      ia[i] = byteString.charCodeAt(i);
    }
    const blob = new Blob([ab], { type: mimeType });
    return new File([blob], filename, { type: mimeType });
  } catch (e) {
    console.error("Failed to decode base64 string:", e);
    return null;
  }
}
