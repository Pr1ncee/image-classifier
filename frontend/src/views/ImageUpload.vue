<template>
  <div class="container mt-5">
    <image-upload-form
      :categories="categories"
      :selectedCategory="selectedCategory"
      @file-change="handleFileChange"
      @category-change="handleCategoryChange"
      @upload-image="uploadImage"
    />
    <image-preview
      :imageUrl="imageUrl"
      :aiCategory="aiCategory"
      :isLoading="isLoading"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import {ImageUploadResponse} from "@/domain/api/imageUploadResponse";
import ImageUploadForm from "@/components/ImageUploadForm.vue";
import ImagePreview from "@/components/ImagePreview.vue";
import ImageUploadApi from "@/api/ImageUploadApi";
import {CategoryResponse} from "@/domain/api/categoryResponse";

export default defineComponent({
  components: {
    ImageUploadForm,
    ImagePreview,
  },
  setup() {
    const image = ref<File | null>(null);
    const imageUrl = ref<string | undefined>(undefined);
    const categories = ref<string[]>([]);
    const selectedCategory = ref<string>('');
    const aiCategory = ref<string>('');
    const isLoading = ref<boolean>(false);
    const api = new ImageUploadApi();

    const handleFileChange = (file: File | null) => {
      image.value = file;
      imageUrl.value = file ? URL.createObjectURL(file) : undefined;
    };

    const handleCategoryChange = (category: string) => {
      selectedCategory.value = category;
    };

    const fetchCategories = async () => {
      try {
        const response: CategoryResponse = await api.fetchCategories();
        categories.value = response.body || [];
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    };

    const uploadImage = async () => {
      if (!image.value || !selectedCategory.value) {
        alert('Please select an image and a category.');
        return;
      }
      const formData = new FormData();
      formData.append('image', image.value);
      formData.append('category_by_user', selectedCategory.value);

      isLoading.value = true;
      aiCategory.value = '';

      try {
        const response: ImageUploadResponse = await api.uploadImage(formData);
        aiCategory.value = response.body.category_by_ai;
      } catch (error) {
        console.error('Error uploading image:', error);
      } finally {
        isLoading.value = false;
      }
    };

    fetchCategories();

    return {
      image,
      imageUrl,
      categories,
      selectedCategory,
      aiCategory,
      isLoading,
      handleFileChange,
      handleCategoryChange,
      uploadImage,
    };
  },
});
</script>

<style scoped>
.container {
  background-color: #c1c1c1;
  width: 600px;
  position: absolute;
  top: 43%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 10px;
  border-radius: 10px;
  text-align: center;
}
</style>
