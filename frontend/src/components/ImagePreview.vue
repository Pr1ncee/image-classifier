<template>
  <div v-if="imageUrl">
    <h2 class="preview_label">Image Preview:</h2>
    <img :src="imageUrl" alt="Image Preview" class="img-fluid" />
    <div class="mt-3 text-center">
      <div v-if="isLoading" class="loading-circle mx-auto"></div>
      <div v-else>
        <h3 v-if="aiCategory">Predicted Category: {{ aiCategory }}</h3>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  props: {
    imageUrl: String,
    aiCategory: String,
    isLoading: Boolean
  },
});
</script>

<style scoped>
.img-fluid {
  margin-top: 30px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.preview_label {
  margin-top: 30px;
}
.loading-circle {
  width: 50px;
  height: 50px;
  border: 5px solid #f3f3f3;
  border-top: 5px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 20px auto;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
