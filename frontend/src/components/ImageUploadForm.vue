<template>
  <div>
    <h1 id="predict_image_category">Predict Image Category</h1>
    <form @submit.prevent="uploadImage">
      <div class="form-group">
        <label for="image">Select Image</label>
        <input type="file" class="form-control" id="image" @change="onFileChange" />
      </div>
      <div class="form-group">
        <label for="category">Select Category</label>
        <select class="form-control" id="category" v-model="internalSelectedCategory" @change="onCategoryChange">
          <option v-for="category in categories" :key="category" :value="category">{{ category }}</option>
        </select>
      </div>
      <button type="submit" class="btn btn-primary">Upload</button>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch, PropType } from 'vue';

export default defineComponent({
  props: {
    categories: {
      type: Array as PropType<string[]>,
      required: true,
    },
    selectedCategory: {
      type: String,
      required: true,
    },
  },
  emits: ['file-change', 'category-change', 'upload-image'],
  setup(props, { emit }) {
    const internalSelectedCategory = ref<string>(props.selectedCategory);

    watch(() => props.selectedCategory, (newCategory) => {
      internalSelectedCategory.value = newCategory;
    });

    const onFileChange = (event: Event) => {
      const file = (event.target as HTMLInputElement).files?.[0] || null;
      emit('file-change', file);
    };

    const onCategoryChange = () => {
      emit('category-change', internalSelectedCategory.value);
    };

    const uploadImage = () => {
      emit('upload-image');
    };

    return {
      internalSelectedCategory,
      onFileChange,
      onCategoryChange,
      uploadImage,
    };
  },
});
</script>

<style scoped>
#predict_image_category {
  margin-bottom: 20px;
  text-align: center;
}
</style>
