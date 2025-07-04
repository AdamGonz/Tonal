'use client'

import { useState } from "react"
import { format } from "date-fns"
import { ChevronDownIcon } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import {Sun, Star, BookOpen } from "lucide-react"
import { Label } from "@/components/ui/label"
import { getAztecYearEmoji } from "@/lib/utils"


import {Popover, PopoverTrigger, PopoverContent,} from "@/components/ui/popover"
import {Card, CardContent, CardHeader, CardTitle, } from "@/components/ui/card"


export default function Home() {
  const [open, setOpen] = useState(false)
  const [date, setDate] = useState<Date | undefined>()
  const [result, setResult] = useState<any>(null)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!date) return

    const formattedDate = date.toISOString().split('T')[0] // YYYY-MM-DD

    try {
      const res = await fetch(`http://localhost:5000/aztec-date?date=${formattedDate}`)
      const data = await res.json()
      setResult(data)
    } catch (err) {
      console.error('Error fetching Aztec date:', err)
    }
  }

  return (
    <main className="min-h-screen relative">
      <div
        className="fixed inset-0 w-full h-full bg-center bg-no-repeat"
        style={{
          backgroundImage: "url('/Tonal_Background.png?height=1080&width=1920')",
          backgroundSize: "cover",
          backgroundPosition: "center center",
        }}
      />
      <div className="fixed inset-0 bg-black/20" />
      
      {/* Main Content */}
      <div className="relative z-10">
        <div className="container mx-auto px-4 py-8 max-w-6xl">
          {/* Header with Glass Panel */}
          <div className="text-center mb-12">
            {/* Glass Panel behind title */}
            <div className="inline-block p-8 rounded-3xl bg-white/0 backdrop-blur-sm border border-white/30 shadow-2xl mb-4">
              <h1 className="text-4xl md:text-5xl font-bold text-white mb-4 drop-shadow-lg">
                Aztec Calendar Converter
              </h1>
              <p className="text-lg text-white/90 max-w-2xl mx-auto drop-shadow-md">
                Discover the sacred meaning of any date in the ancient Aztec calendar system
              </p>
            </div>
          </div>
          <div className="relative z-10">
            <div className="max-w-xl mx-auto flex flex-col items-center space-y-6 text-center">
              <Label htmlFor="date" className="px-1">
                SELECT A DATE 
              </Label>
              <Popover open={open} onOpenChange={setOpen}>
                <PopoverTrigger asChild>
                  <Button
                    variant="outline"
                    id="date"
                    className="w-48 justify-between font-normal"
                  >
                    {date ? date.toLocaleDateString() : "Select date"}
                    <ChevronDownIcon />
                  </Button>
                </PopoverTrigger>
                <PopoverContent className="w-auto overflow-hidden p-0" align="start">
                  <Calendar
                    mode="single"
                    selected={date}
                    captionLayout="dropdown"
                    onSelect={(date) => {
                      setDate(date)
                      setOpen(false)
                    }}
                  />
                </PopoverContent>
              </Popover>
              <form onSubmit={handleSubmit} className="mb-6 space-y-4">
                <Button type="submit" className="bg-black text-white px-4 py-2 rounded">
                  CONVERT
                </Button>
              </form>

              {result && (
                <div className="space-y-8">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                    {/* Xiuhpohualli (Solar Month) */}
                    <Card className="shadow-lg border-0 bg-white/90 backdrop-blur-sm hover:shadow-xl transition-shadow duration-300">
                      <CardHeader className="pb-4">
                        <div className="flex items-center gap-3">
                          <div className="p-2 bg-amber-100 rounded-lg">
                            <Sun className="h-6 w-6 text-amber-600" />
                          </div>
                          <CardTitle className="text-xl text-gray-900">Xiuhpohualli</CardTitle>
                        </div>
                        <p className="text-sm text-gray-600">Solar Month</p>
                      </CardHeader>
                      <CardContent>
                        <div className="text-center">
                          <div className="text-lg font-bold text-amber-600 mb-2">{result.aztec_month}</div>
                          <div className="w-16 h-16 mx-auto bg-amber-50 rounded-full flex items-center justify-center mb-3">
                            <span className="text-2xl">☀️</span>
                          </div>
                          <div className="space-y-1 text-sm text-gray-600">
                            <p>
                              <strong>English:</strong> {result.aztec_month_english}
                            </p>
                            <p>
                              <strong>Spanish:</strong> {result.aztec_month_spanish}
                            </p>
                          </div>
                        </div>
                      </CardContent>
                    </Card>

                    {/* Aztec Year Sign */}
                    <Card className="shadow-lg border-0 bg-white/90 backdrop-blur-sm hover:shadow-xl transition-shadow duration-300">
                      <CardHeader className="pb-4">
                        <div className="flex items-center gap-3">
                          <div className="p-2 bg-blue-100 rounded-lg">
                            <Star className="h-6 w-6 text-blue-600" />
                          </div>
                          <CardTitle className="text-xl text-gray-900">Year Sign</CardTitle>
                        </div>
                        <p className="text-sm text-gray-600">Year Bearer</p>
                      </CardHeader>
                      <CardContent>
                        <div className="text-center">
                          <div className="text-3xl font-bold text-blue-600 mb-2">
                            {result.aztec_year_number} {result.aztec_year_symbol}
                          </div>
                          <div className="w-16 h-16 mx-auto bg-blue-50 rounded-full flex items-center justify-center mb-3">
                            <span className="text-2xl">{getAztecYearEmoji(result.aztec_year_symbol)}</span>
                          </div>
                          <p className="text-sm text-gray-600">52-year cycle bearer</p>
                        </div>
                      </CardContent>
                    </Card>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}
