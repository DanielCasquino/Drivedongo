export class CustomError extends Error {
  constructor(statusCode, body) {
    super(body); // Pass the body as the error message
    this.statusCode = statusCode;
    this.body = body;
  }

  static fromJSON(json) {
    return new CustomError(json.statusCode, json.body);
  }
}
