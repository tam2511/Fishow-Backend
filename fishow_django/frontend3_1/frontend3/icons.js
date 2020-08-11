const result = []
const sizesApple = [
  '57x57',
  '60x60',
  '72x72',
  '76x76',
  '114x114',
  '120x120',
  '144x144',
  '152x152',
  '180x180',
]
const defaultSizes = ['32x32', '96x96', '16x16']
const templateApple = (size) => {
  return {
    rel: 'apple-touch-icon',
    sizes: size,
    type: 'image/x-icon',
    href: `/apple-icon-${size}.png`,
  }
}
const templateDesktop = (size) => {
  return {
    rel: 'icon',
    type: 'image/png',
    sizes: size,
    href: `/favicon-${size}.png`,
  }
}

sizesApple.map((x) => result.push(templateApple(x)))
defaultSizes.map((x) => result.push(templateDesktop(x)))

result.push(
  {
    rel: 'icon',
    type: 'image/png',
    sizes: '192x192',
    href: '/android-icon-192x192.png',
  },
  {
    rel: 'manifest',
    href: '/manifest.json',
  }
)
export default result
