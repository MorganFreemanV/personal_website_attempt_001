<script setup>
import { ref } from "vue";

const todos = ref([
  { id: id++, text: "Learn .vue", done: false },
  { id: id++, text: "Learn js", done: false },
  { id: id++, text: "Learn html", done: false },
]);
</script>

<template>
  <ul>
    <li v-for="todo in todos" :key="todo.id"></li>
  </ul>
</template>

<style>
.id {
  text-decoration: line-through;
}
</style>
