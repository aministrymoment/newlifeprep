// US Letter Avery address label sheets. Sizes are in inches. Several Avery numbers share one layout.
export type Sheet = { cols: number; rows: number; w: number; h: number; left: number; top: number; pitchX: number; pitchY: number; fontPt: number };

const L5160: Sheet = { cols: 3, rows: 10, w: 2.625, h: 1, left: 0.1875, top: 0.5, pitchX: 2.75, pitchY: 1, fontPt: 10 };
const L5161: Sheet = { cols: 2, rows: 10, w: 4, h: 1, left: 0.15625, top: 0.5, pitchX: 4.1875, pitchY: 1, fontPt: 11 };
const L5162: Sheet = { cols: 2, rows: 7, w: 4, h: 1 + 1 / 3, left: 0.15625, top: 0.8333, pitchX: 4.1875, pitchY: 1 + 1 / 3, fontPt: 12 };
const L5163: Sheet = { cols: 2, rows: 5, w: 4, h: 2, left: 0.15625, top: 0.5, pitchX: 4.1875, pitchY: 2, fontPt: 13 };
const L5164: Sheet = { cols: 2, rows: 3, w: 4, h: 3 + 1 / 3, left: 0.15625, top: 0.5, pitchX: 4.1875, pitchY: 3 + 1 / 3, fontPt: 14 };

export const AVERY: Record<string, Sheet> = {
  '5160': L5160, '5260': L5160, '8160': L5160, '5960': L5160,
  '5161': L5161, '5261': L5161, '8161': L5161,
  '5162': L5162, '5262': L5162, '8162': L5162,
  '5163': L5163, '5263': L5163, '8163': L5163,
  '5164': L5164, '5264': L5164, '8164': L5164,
};
export const AVERY_NUMBERS = Object.keys(AVERY);
export const perSheet = (s: Sheet) => s.cols * s.rows;
