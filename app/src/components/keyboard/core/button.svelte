<script lang="ts">
  import { createEventDispatcher } from 'svelte';

  // props
  export let char: string;

  // state
  let pressed: boolean = false;
	
	const dispatch = createEventDispatcher();

  // handlers
  function toggle(direction: 'down' | 'up') {
    return () => {  
      pressed = direction === 'down';
    };
  }

  function dispatchClick() {
    dispatch('click');
  }
</script>

<button
  class={$$props.class}
  class:pressed={pressed}
  on:click={dispatchClick}
  on:mousedown={toggle('down')}
  on:mouseup={toggle('up')}
>
  {char}
</button>

<style lang="scss">
	button {
    padding: .75rem 1rem;
    color: #333;
    font-size: 1rem;
    border: none;
    border-radius: 5px;
    outline: none;
		background-color: rgb(211, 214, 218);
    transition: background-color .2s ease-in-out, transform .2s ease-in-out;
    cursor: pointer;

    &.pressed {
      background-color: #f5f5f5;
      transform: scale(.95);
    }
	}
</style>