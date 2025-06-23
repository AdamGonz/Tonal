import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function getAztecYearEmoji(symbol: string): string {
  switch (symbol) {
    case "Tochtli":
      return "🐇"
    case "Acatl":
      return "🌾"
    case "Tecpatl":
      return "🔪"
    case "Calli":
      return "🏠"
    default:
      return "❓"
  }
}
