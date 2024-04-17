<template>
<a href="{% url 'recipes:ingredient_list' %}">Ingredients list</a><br/>
<a href="{% url 'recipes:ingredient_create' %}">New Ingredient</a><br/>
<a href="{% url 'recipes:recipe_create' %}">New Recipe</a><br/><br/>
    <h1>{{ this.recipe.name }}</h1>
    Ingredients:<br/>
    <span v-for="ingredient in this.recipe.ingredients">
        {{ingredient.name}}<br/></span>
    <br/>
    Food Description: {{this.recipe.foodDescription}}<br/>
    Recipe: {{this.recipe.recipe}}<br/>
</template>

<script>
    
    export default {
      name: 'App',
      components: {
      },
      data: function() {
          return {
            recipe_error: [],
            recipe_id: ext_recipe_id,
            recipe_detail_js_url: ext_recipe_detail_js_url,
            recipe_list_url: ext_recipe_list_url,
            recipe_update_url: ext_recipe_update_url,
            recipe_delete_url: ext_recipe_delete_url,
            recipe: {}
        }},
        methods: {
            get_recipe_info(){
                fetch(this.recipe_detail_js_url,
                    {
                        method: "get",
                        credentials: 'same-origin'
                    }
                ).then(function(response) {
                    console.log('response', response)
                    return response.json()}).then(this.assign_recipe).catch(
                        (error) => { 
                        console.log('error', error)
                        this.recipe_error=["error when loading recipe information"]
            })
            },
            assign_recipe(recipe_json) {
                console.log('json', recipe_json)
                this.recipe = recipe_json['recipe']
            },
        },
        computed: {
        },
        beforeMount() {
            this.get_recipe_info()
        },
    }
    </script>