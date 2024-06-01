export interface ImageUploadResponseBody {
  id: number;
  image: string;
  category_by_user: string;
  category_by_ai: string;
}

export interface ImageUploadResponse {
  status: number;
  body: ImageUploadResponseBody;
}
