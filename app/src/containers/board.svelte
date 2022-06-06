<script lang="ts">
	import { EMPTY_CELL_VALUE, MAX_COLUMN_SIZE, MAX_ROW_SIZE } from '../constants';
	import Matrix from '../components/matrix/matrix.svelte';
	import Keyboard from '../components/keyboard/keyboard.svelte';
	import { findIndexBottomTop } from '../helpers/array-utils';

	let boardState: BoardMatrix = Array(MAX_COLUMN_SIZE).fill(null).map(() => ({
		cells: Array(MAX_ROW_SIZE).fill(EMPTY_CELL_VALUE),
		commited: false,
	}));

	function handleKeyboardPress({ detail: { char } }: CustomEvent<{ char: string }>) {
		if (char === 'ENTER') {
			const lastWorkingRow = findIndexBottomTop(boardState, (row) => {
				const usedSpaces = row.cells.filter(Boolean).length;
									
				return usedSpaces > 0;
			});

			// error if not completed
			// error if wrong guess
			// commit the row if completed
		} else if (char === 'BACK') {
			const lastWorkingRow = findIndexBottomTop(boardState, (row) => {
				const usedSpaces = row.cells.filter(Boolean).length;
									
				return usedSpaces > 0 && usedSpaces <= MAX_ROW_SIZE;
			});
				
			if (lastWorkingRow > -1) {
				const indexToDelete = findIndexBottomTop(boardState[lastWorkingRow].cells, Boolean);

				boardState[lastWorkingRow].cells[indexToDelete] = EMPTY_CELL_VALUE;
				boardState = boardState.slice();
			}

			// do not delete if row is commited
		} else {
			const lastWorkingRow = boardState.findIndex((row) => row.cells.filter(Boolean).length < MAX_ROW_SIZE);

			if (lastWorkingRow !== -1) {
				const indexToFill = boardState[lastWorkingRow].cells.findIndex((e) => !e);
				boardState[lastWorkingRow].cells[indexToFill] = char;
				boardState = boardState;
			}

			// do not write on new row unless current row is commited
		}
	}
</script>

<Matrix class="matrix-wrapper" boardState={boardState} />
<Keyboard on:click={handleKeyboardPress} />

<style lang="scss">
	.matrix-wrapper {
		margin-bottom: 1rem;
	}
</style>
