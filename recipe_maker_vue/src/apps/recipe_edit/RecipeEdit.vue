<template>
    <div>
        <h1>Create Recipes Below!</h1>
    </div>

    <div>
        <form method="post" class="form">
            <input type="hidden" name="csrfmiddlewaretoken"
                   v-bind:value="csrf_token">
            <p>
                <label for="id_name">Recipe Name:</label>
                <input type="text" maxlength="100" required="" id="id_name">
            </p>

            <p>
                <label for="id_director">Food Description:</label>
                <input type="text" maxlength="500" required="" id="id_food_description">
            </p>

                <button type="submit" class="btn btn-primary">
                    Submit
                </button>                    
        </form>
    </div>

</template>

<script>
export default {
    name: 'App',
  components: {
  },
  props: [
  ],
  data: function() {
    return {
        csrf_token: ext_csrf_token,
    }
  },
  computed: {
  },
  methods: {
  },
  watch: {
  }
}
</script>


