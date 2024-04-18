import 'vite/modulepreload-polyfill';
import { createApp } from 'vue';
import AppCreate from './RecipeCreate.vue'

createApp(AppCreate).mount("#appcreate")