// Turns markdown style text into clean plain text for the tutor chat.
export function plainText(s: string): string {
  return String(s || '')
    .replace(/\r/g, '')
    .replace(/```[a-z]*\n?/gi, '')
    .replace(/\*\*([\s\S]+?)\*\*/g, '$1')
    .replace(/__([\s\S]+?)__/g, '$1')
    .replace(/^\s{0,3}#{1,6}\s*/gm, '')
    .replace(/^\s*[*\-]\s+/gm, '• ')
    .replace(/\*([^*\n]+?)\*/g, '$1')
    .replace(/`([^`]*)`/g, '$1')
    .replace(/\*+/g, '')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
}
