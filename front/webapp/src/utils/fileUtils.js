import axios from "axios";
import { CustomError } from "./errorUtils";
import { checkAuth } from "./authUtils";
import { useNotificationStore } from "@/stores/notification-store";

export async function sendFile(metadata, b64){
    try{
        const uid = await checkAuth();
        const uploadResponse = await axios.post(
            "https://ao9ww2ed5d.execute-api.us-east-1.amazonaws.com/dev/file/upload",
            {
              user_id: uid,
              file_name: metadata.name,
              file_content: b64
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
                const notiStore = useNotificationStore();
                notiStore.show(formattedResponse.statusCode, formattedResponse.body);
              break;
            default:
                throw CustomError.fromJSON(formattedResponse);
          }
    }
    catch(e){
        const notiStore = useNotificationStore();
        notiStore.show(500, "Terrible oremos");
    }
}