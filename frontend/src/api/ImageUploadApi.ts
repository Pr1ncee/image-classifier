import FetchHttpClient from "@/api/FetchHttpClient";

export default class ImageUploadApi {
  private httpClient: FetchHttpClient;
  private API_URL = 'http://localhost:8000';

  constructor() {
    this.httpClient = new FetchHttpClient();
  }

  async fetchCategories(): Promise<any> {
    return await this.httpClient.makeApiRequest(
      `${this.API_URL}/api/v1/categories/`,
      'GET'
    );
  }

  async uploadImage(formData: FormData): Promise<any> {
    return await this.httpClient.makeApiRequest(
      `${this.API_URL}/api/v1/images/`,
      'POST',
      formData,
      true
    );
  }
}
