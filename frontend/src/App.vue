<template>
  <div id="app">
    <ImageUpload />
  </div>
</template>

<script lang="ts">

import ImageUpload from "@/views/ImageUpload.vue";

export default {
  name: 'Image Category Classifier',
  components: {
    ImageUpload,
  },
};
</script>

<style>
@import 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css';
</style>
