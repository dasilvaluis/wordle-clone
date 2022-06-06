<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import letters from '../../data/ro-letters.json';
	import Button from './core/button.svelte';
	
	const dispatch = createEventDispatcher();

	function dispatchCharClick(char: string) {
		return () => {
			dispatch('click', { char });
		};
	}
</script>

<div class="keyboard">
	{#each letters.rows as lettersRow}
		<div class="keyboard-row">
			{#each lettersRow as letter}
				<Button class="keyboard-button" char={letter} on:click={dispatchCharClick(letter)} />
			{/each}
		</div>
	{/each}
</div>

<style lang="scss">
	.keyboard {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;

		&-row > :global(&-button) {
			margin: 0.15rem;
		}
	}
</style>
