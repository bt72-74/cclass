import React from 'react'

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  title?: string
  subtitle?: string
}

export const Card = React.forwardRef<HTMLDivElement, CardProps>(
  ({ title, subtitle, children, className, ...props }, ref) => {
    return (
      <div
        ref={ref}
        className={`
          bg-white rounded-lg p-6 shadow-md
          border border-gray-100
          hover:shadow-lg transition-shadow duration-200
          ${className}
        `}
        {...props}
      >
        {title && (
          <div className="mb-4">
            <h3 className="text-lg font-semibold text-gray-900">{title}</h3>
            {subtitle && <p className="text-sm text-gray-500 mt-1">{subtitle}</p>}
          </div>
        )}
        {children}
      </div>
    )
  }
)

Card.displayName = 'Card'
