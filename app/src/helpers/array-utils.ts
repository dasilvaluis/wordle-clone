export function rightPadArray<T>(arr: T[], length: number, value: T): T[] {
  const result = arr.slice();
  while (result.length < length) {
    result.push(value);
  }
  return result;
}

export function findIndexBottomTop<T>(arr: T[], predicate: (item: T, index: number, obj: T[]) => boolean): number {
  const lastWorkingRowReverse = arr
    .slice()
    .reverse()
    .findIndex(predicate);

  return lastWorkingRowReverse < 0 ? -1 : arr.length - 1 - lastWorkingRowReverse;
}
