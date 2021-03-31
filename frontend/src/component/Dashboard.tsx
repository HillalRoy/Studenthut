import React, { useEffect, useMemo, useRef, useState } from 'react'
import './Dashboard.scss'


export const CreateClass: React.FC = () => {
  return (
  <>




  </>
  )
}

export const Dashboard: React.FC = () => {
  const [lines, setLines]= useState<string[]>([])
  const timeline = useRef<HTMLDivElement>()
  const [timelineWidth, setTimelineWidth] = useState(0)
  const classesElRef = useRef<HTMLDivElement>()
  const activeLine = useRef<HTMLDivElement>()

  useEffect(() => {
    const handler = () => setTimelineWidth(timeline.current?.offsetWidth ?? 0)
    window.addEventListener('resize', handler)
    handler()
    return () => window.removeEventListener('resize', handler)
  }, [timeline.current])

  useEffect(() => {
    const hourWidth = timelineWidth / 24
    const minuteWidth = hourWidth / 60
    const intervalFun = () => {

      const date = new Date()
      const hour = date.getHours()
      const minute = date.getMinutes()
      const scrollPos = hour * hourWidth + minute * minuteWidth

      if (classesElRef.current)
        {classesElRef.current.scrollLeft = scrollPos - hourWidth/2}
      if(activeLine.current)
        {activeLine.current.style.left = `${scrollPos}px`}
    }
    const interval = setInterval(intervalFun, 1000 * 60)
    intervalFun()

    const mouseWheelHandler  = (event: WheelEvent) => {
      event.preventDefault();
      (event.target as HTMLDivElement).scrollLeft += event.deltaY * 2.5
    }
    if(classesElRef.current)
    {classesElRef.current.addEventListener('wheel', mouseWheelHandler)}

    return () => {
      clearInterval(interval)
      classesElRef.current?.removeEventListener('wheel', mouseWheelHandler)
    }
  }, [classesElRef.current, activeLine.current,timelineWidth])


  useMemo(() => {
    const lines = []
    for (let i = 0; i < 24 * 2; i++) {
      const hour = Math.floor(i / 2) % 12
      lines.push(`${hour === 0 ? 12 : hour}:${i & 0x1 ? '30' : '00'} ${i / 2 < 12 ? 'am' : 'pm'}`)
    }
    setLines(lines)
  }, [setLines])

  return (
    <div>
      <h1>Dashboard</h1>
      <div className="timeline-header"></div>
      <div className="classes" ref={classesElRef as React.MutableRefObject<HTMLDivElement>}>
        <div className="timeline" ref={timeline as React.MutableRefObject<HTMLDivElement>}>
          <div className="class-items"></div>
          <div className="lines">

            {
              lines.map((el, i) =>
                <div className="line"
                  key={el}
                  style={{ left: (i) * timelineWidth / (lines.length) }}>
                  {el}
                </div>)
            }
            <div ref={activeLine as React.MutableRefObject<HTMLDivElement>} className="line active"></div>
          </div>
        </div>
      </div>
    </div>
  )
}