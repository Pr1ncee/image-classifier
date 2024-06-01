import {ApiResponse} from "@/domain/api/apiResponse";


export default class FetchHttpClient {
  async makeApiRequest<T>(url: string, method: string, body: any = null, isFormData: boolean = false): Promise<ApiResponse<T>> {
    const headers: HeadersInit = isFormData ? {} : { 'Content-Type': 'application/json' };

    const requestOptions: RequestInit = {
      method: method,
      headers: headers,
      body: body
    };

    try {
      const response = await fetch(url, requestOptions);
      return {
        status: response.status,
        body: await response.json().catch(() => null)
      };
    } catch (error) {
      throw new Error('API request failed');
    }
  }
}