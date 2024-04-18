<template>
    <div>
        <h1>Create Recipes Below!</h1>
    </div>

    <div>
        <form method="post" class="form">
            <input type="hidden" name="csrfmiddlewaretoken"
                   v-bind:value="csrf_token">
            <p>
                <label for="id_name">Recipe Title: </label> &nbsp;
                <input type="text" name="name" v-model="title" maxlength="100"
                required="" id="id_name">
            </p>
            
            <p>
                <label for="id_ingredients">Ingredients:</label>
                <select hidden name="ingredients"  id="id_ingredients" multiple="">
                    <option v-for="ingredient in ingredient_list" :value="ingredient.id" selected=""></option>
                </select>
                <multiselect v-model="ingredient_list" :options="ingredient_list_source" :multiple="true" :close-on-select="false" :clear-on-select="false" :preserve-search="true" placeholder="Choose the ingredients" label="name" track-by="name" :preselect-first="true" style="display:inline-block;width: 300px;padding-bottom:10px;padding-left:10px">
                    <template slot="selection" slot-scope="{ values, search, isOpen }"><span class="multiselect__single" v-if="values.length" v-show="!isOpen">{{ values.length }} options selected</span></template>
                </multiselect>
            </p>

            <p>
                <label for="id_foodDescription">Description: </label>&nbsp;
                <input type="hidden" :value="foodDescription" name="foodDescription" value=""
                maxlength="5000" required="" id="id_foodDescription"  >
                <textarea v-model="foodDescription" name="foodDescription" cols="50" maxlength="5000" rows="3"> </textarea>
            </p>

            <p>
                <label for="id_recipe">Recipe: </label>&nbsp;
                <input type="hidden" :value="recipe" name="recipe" value=""
                maxlength="5000" required="" id="id_recipe"  >
                <textarea v-model="recipe" name="recipe" cols="50" maxlength="5000" rows="3"> </textarea>
            </p>

                <button type="submit" class="btn btn-primary">
                    Submit
                </button>                    
        </form>
    </div>

</template>

<script>
import Multiselect from 'vue-multiselect'
    export default {
        name: 'AppCreate',
        components: {
            Multiselect,
        },
        data: function() {
            return {
                ingredient: null,
                csrf_token: window.ext_csrf_token,
                foodDescription: null,
                recipe: null,
                recipe_dico: [],
                title: null,
                ingredient_list_source: (window.ext_ingredient_list != undefined ) ? window.ext_ingredient_list: [],
                ingredient_list: [],
                window: window,
            }
        },
        methods: {

        },
        computed: {

        },
        mounted(){
            this.csrf_token=ext_csrf_token;  
            this.ingredient_list_source= ext_ingredient_list;
        },
    }
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>
