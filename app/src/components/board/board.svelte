<script lang="ts">
	import { EMPTY_CELL_VALUE } from '../../constants';
	import Cell from './core/cell.svelte';

	export let boardState: BoardMatrix;
</script>

<div class="matrix">
	{#each boardState as row}
		<div class="matrix-row">
			{#each row.cells as letter}
				<Cell class="matrix-item" char={letter || EMPTY_CELL_VALUE} />
			{/each}
		</div>
	{/each}
</div>

<style lang="scss">
	.matrix {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;

		&-row {
			display: flex;
			flex-direction: row;
			align-items: center;
			justify-content: center;
		}

		&-row > :global(&-item) {
			margin: 0.15rem;
		}
	}
</style>
