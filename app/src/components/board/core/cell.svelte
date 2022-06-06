<script lang="ts">
import { compute_rest_props } from "svelte/internal";

  export let char: string = '';
</script>

<div class={`cell ${$$props.class}`}>
  {char}
</div>

<style lang="scss">
  .cell {
    width: 3.5rem;
    height: 3.5rem;
    border: 2px solid #d3d6da;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Helvetica', 'Arial', 'sans-serif';
  }
</style>
