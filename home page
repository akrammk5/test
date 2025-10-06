"use client";

import { Button } from "/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "/components/ui/card";
import { Input } from "/components/ui/input";
import {
  Star,
  Book,
  Heart,
  Palette,
  Gift,
  Users,
  Sparkles,
  ShoppingCart,
  Check,
  ChevronRight,
  Globe,
  Award,
  TrendingUp,
} from "lucide-react";
import { useState, useEffect } from "react";
import { motion, useScroll, useTransform } from "framer-motion";

export default function PolishColoringBookLanding() {
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });
  const { scrollYProgress } = useScroll();
  const bookRotateX = useTransform(scrollYProgress, [0, 1], [0, 360]);
  const bookRotateY = useTransform(scrollYProgress, [0, 1], [0, 180]);

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      setMousePosition({
        x: (e.clientX / window.innerWidth - 0.5) * 20,
        y: (e.clientY / window.innerHeight - 0.5) * 20,
      });
    };
    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, []);

  const features = [
    {
      icon: Book,
      title: "45 Hand-Drawn Pages",
      description:
        "Bold, thick lines perfect for markers, pens, and pencils—designed for easy, stress-free coloring",
    },
    {
      icon: Palette,
      title: "Graffiti-Style Art",
      description:
        "Modern, playful designs featuring popular Polish names in stunning urban art aesthetics",
    },
    {
      icon: Heart,
      title: "Stress Relief",
      description:
        "Therapeutic coloring experience that promotes mindfulness, relaxation, and creative expression",
    },
    {
      icon: Globe,
      title: "Cultural Connection",
      description:
        "Explore the beauty of Polish names while learning about Polish culture in a fun, interactive way",
    },
    {
      icon: Users,
      title: "All Ages Welcome",
      description:
        "Perfect for kids (3-18), teens, and adults—whether learning Polish or just relaxing",
    },
    {
      icon: Gift,
      title: "Perfect Gift",
      description:
        "Thoughtful, personalized present for anyone with Polish heritage or a love for unique names",
    },
  ];

  const benefits = [
    "Single-sided pages prevent bleed-through",
    "8.5 x 8.5 inch square format for easy handling",
    "Protective sheet included for markers",
    "Suitable for all skill levels",
    "Family bonding activity",
    "Educational and entertaining",
  ];

  const testimonials = [
    {
      name: "Maria K.",
      text: "This book is a game-changer! I love how personalized it feels—each page brings out my creativity!",
      rating: 5,
    },
    {
      name: "Anna W.",
      text: "The designs are just stunning! A true stress reliever for me and my kids. Highly recommend!",
      rating: 5,
    },
    {
      name: "Piotr S.",
      text: "My Polish name looks AMAZING in graffiti style. Perfect gift for anyone with a unique name!",
      rating: 5,
    },
  ];

  const polishNames = [
    "Zofia",
    "Jan",
    "Maria",
    "Piotr",
    "Anna",
    "Jakub",
    "Katarzyna",
    "Michał",
  ];

  return (
    <main className="min-h-screen overflow-x-hidden bg-background">
      {/* Animated Background */}
      <div className="fixed inset-0 -z-10 bg-gradient-to-br from-background via-accent/5 to-background">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(239,68,68,0.05),transparent_50%)]" />
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_80%_20%,rgba(255,255,255,0.03),transparent_50%)]" />
        
        {/* Floating Particles */}
        {[...Array(20)].map((_, i) => (
          <motion.div
            key={i}
            className="absolute h-2 w-2 rounded-full bg-primary/20"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
            }}
            animate={{
              y: [0, -30, 0],
              x: [0, Math.random() * 20 - 10, 0],
              opacity: [0.2, 0.5, 0.2],
              scale: [1, 1.5, 1],
            }}
            transition={{
              duration: 3 + Math.random() * 2,
              repeat: Infinity,
              delay: Math.random() * 2,
            }}
          />
        ))}
      </div>

      {/* Hero Section with 3D Book */}
      <section className="relative min-h-screen overflow-hidden py-20 lg:py-32">
        <div className="container relative z-10 mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 items-center gap-12 lg:grid-cols-2">
            {/* Left Content */}
            <motion.div
              initial={{ opacity: 0, x: -50 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8 }}
              className="text-center lg:text-left"
            >
              <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.2 }}
                whileHover={{ scale: 1.05 }}
                className="mb-4 inline-flex items-center gap-2 rounded-full border border-primary/20 bg-gradient-to-r from-primary/10 to-red-600/10 px-4 py-2 text-sm font-semibold text-primary shadow-lg"
              >
                <motion.div
                  animate={{ rotate: [0, 360] }}
                  transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
                >
                  <Sparkles className="h-4 w-4" />
                </motion.div>
                <span>🎨 New Release 2025 ✨</span>
              </motion.div>

              <h1 className="mb-6 text-4xl font-black leading-tight text-foreground sm:text-5xl lg:text-7xl">
                Transform Stress Into
                <span className="block bg-gradient-to-r from-red-500 to-red-700 bg-clip-text text-transparent">
                  Creative Magic
                </span>
              </h1>

              <p className="mb-8 text-xl leading-relaxed text-muted-foreground">
                Discover the ultimate stress relief coloring book featuring{" "}
                <span className="font-bold text-foreground">
                  45 hand-drawn Polish names
                </span>{" "}
                in stunning graffiti-style art. Perfect for all ages, from kids
                to adults!
              </p>

              <div className="mb-8 flex flex-wrap items-center justify-center gap-4 lg:justify-start">
                <motion.div 
                  className="flex items-center gap-1 rounded-full bg-yellow-50 px-3 py-1"
                  whileHover={{ scale: 1.05 }}
                >
                  {[...Array(5)].map((_, i) => (
                    <motion.div
                      key={i}
                      initial={{ scale: 0 }}
                      animate={{ scale: 1 }}
                      transition={{ delay: i * 0.1 }}
                    >
                      <Star
                        className="h-5 w-5 fill-yellow-400 text-yellow-400"
                      />
                    </motion.div>
                  ))}
                  <span className="ml-2 font-semibold text-foreground">
                    5.0 ⭐
                  </span>
                </motion.div>
                <div className="h-6 w-px bg-border" />
                <div className="flex items-center gap-2 text-sm text-muted-foreground">
                  <Heart className="h-4 w-4 fill-red-500 text-red-500" />
                  <span>Loved by families worldwide 🌍</span>
                </div>
              </div>

              <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-center lg:justify-start">
                <Button
                  size="lg"
                  className="group bg-gradient-to-r from-red-600 to-red-700 text-lg font-bold text-white shadow-lg shadow-red-500/30 transition-all hover:scale-105 hover:shadow-xl hover:shadow-red-500/40"
                  onClick={() => window.open('https://www.amazon.com/Stress-Relief-Featuring-Relaxation-Creativity/dp/B0F475VKY9', '_blank')}
                >
                  <ShoppingCart className="mr-2 h-5 w-5" />
                  Buy Now - Only $6.99
                  <ChevronRight className="ml-2 h-5 w-5 transition-transform group-hover:translate-x-1" />
                </Button>
                <Button
                  size="lg"
                  variant="outline"
                  className="border-2 border-primary text-lg font-semibold transition-all hover:scale-105"
                  onClick={() => window.open('https://www.amazon.com/Stress-Relief-Featuring-Relaxation-Creativity/dp/B0F475VKY9', '_blank')}
                >
                  <Book className="mr-2 h-5 w-5" />
                  Preview on Amazon
                </Button>
              </div>

              <div className="mt-8 flex flex-wrap items-center justify-center gap-6 lg:justify-start">
                <motion.div 
                  className="flex items-center gap-2 rounded-lg bg-green-50 px-3 py-2 text-sm font-medium text-green-700"
                  whileHover={{ scale: 1.05 }}
                >
                  <Check className="h-5 w-5 text-green-600" />
                  <span>🚚 Free Shipping</span>
                </motion.div>
                <motion.div 
                  className="flex items-center gap-2 rounded-lg bg-blue-50 px-3 py-2 text-sm font-medium text-blue-700"
                  whileHover={{ scale: 1.05 }}
                >
                  <Check className="h-5 w-5 text-blue-600" />
                  <span>↩️ 30-Day Returns</span>
                </motion.div>
                <motion.div 
                  className="flex items-center gap-2 rounded-lg bg-purple-50 px-3 py-2 text-sm font-medium text-purple-700"
                  whileHover={{ scale: 1.05 }}
                >
                  <Check className="h-5 w-5 text-purple-600" />
                  <span>🔒 Secure Payment</span>
                </motion.div>
              </div>
            </motion.div>

            {/* Right - 3D Book Animation */}
            <motion.div
              className="relative flex items-center justify-center"
              style={{
                rotateX: mousePosition.y * 0.5,
                rotateY: mousePosition.x * 0.5,
                transformStyle: "preserve-3d",
                perspective: "1000px",
              }}
              transition={{ type: "spring", stiffness: 100, damping: 20 }}
            >
              <motion.div
                className="relative"
                animate={{
                  y: [0, -20, 0],
                  rotateZ: [-2, 2, -2],
                }}
                transition={{
                  duration: 4,
                  repeat: Infinity,
                  ease: "easeInOut",
                }}
              >
                <motion.div 
                  className="relative h-96 w-80 transform-gpu"
                  whileHover={{ 
                    scale: 1.05,
                    rotateY: 15,
                    rotateX: -5,
                    z: 50,
                  }}
                  transition={{ 
                    type: "spring", 
                    stiffness: 300, 
                    damping: 20 
                  }}
                  style={{ transformStyle: "preserve-3d" }}
                >
                  {/* Book Shadow */}
                  <motion.div 
                    className="absolute inset-0 translate-y-8 rounded-2xl bg-black/20 blur-3xl"
                    animate={{ 
                      scale: [1, 1.05, 1],
                      opacity: [0.2, 0.3, 0.2]
                    }}
                    transition={{ duration: 3, repeat: Infinity }}
                  />

                  {/* Book Cover */}
                  <div 
                    className="relative h-full w-full overflow-hidden rounded-2xl border-4 border-white bg-gradient-to-br from-red-50 to-white shadow-2xl"
                    style={{ 
                      transformStyle: "preserve-3d",
                      transform: "translateZ(20px)"
                    }}
                  >
                    <div className="flex h-full flex-col items-center justify-center p-8 text-center">
                      <div className="mb-4 text-6xl font-black text-red-600">
                        🇵🇱 POLSKA
                      </div>
                      <div className="mb-2 text-2xl font-bold text-gray-800">
                        ✨ Stress Relief ✨
                      </div>
                      <div className="mb-6 text-lg text-gray-600">
                        🎨 Coloring Book 🖍️
                      </div>
                      <div className="space-y-2">
                        {polishNames.slice(0, 4).map((name, i) => (
                          <motion.div
                            key={name}
                            initial={{ opacity: 0, x: -20, z: -50 }}
                            animate={{ opacity: 1, x: 0, z: 0 }}
                            transition={{ delay: i * 0.1 }}
                            whileHover={{ 
                              scale: 1.1, 
                              z: 30,
                              backgroundColor: "rgb(254, 226, 226)",
                              boxShadow: "0 10px 30px rgba(239, 68, 68, 0.3)"
                            }}
                            className="rounded bg-red-100 px-4 py-1 text-sm font-semibold text-red-700 cursor-pointer"
                            style={{ transformStyle: "preserve-3d" }}
                          >
                            {name}
                          </motion.div>
                        ))}
                      </div>
                    </div>

                    {/* Polish Flag Accent */}
                    <div className="absolute left-0 top-0 h-1/2 w-full bg-white" />
                    <div className="absolute bottom-0 left-0 h-1/2 w-full bg-red-600" />
                  </div>

                  {/* Floating Elements */}
                  <motion.div
                    className="absolute -right-8 -top-8"
                    animate={{ 
                      rotate: 360,
                      y: [0, -10, 0],
                      scale: [1, 1.1, 1]
                    }}
                    transition={{ 
                      rotate: { duration: 20, repeat: Infinity, ease: "linear" },
                      y: { duration: 3, repeat: Infinity },
                      scale: { duration: 2, repeat: Infinity }
                    }}
                    whileHover={{ scale: 1.3, rotate: 45 }}
                  >
                    <Palette className="h-16 w-16 text-primary opacity-30 drop-shadow-lg" />
                  </motion.div>

                  <motion.div
                    className="absolute -bottom-8 -left-8"
                    animate={{ 
                      rotate: -360,
                      y: [0, 10, 0],
                      scale: [1, 1.15, 1]
                    }}
                    transition={{ 
                      rotate: { duration: 15, repeat: Infinity, ease: "linear" },
                      y: { duration: 2.5, repeat: Infinity },
                      scale: { duration: 2, repeat: Infinity }
                    }}
                    whileHover={{ scale: 1.4, rotate: -45 }}
                  >
                    <Sparkles className="h-12 w-12 text-yellow-400 opacity-40 drop-shadow-lg" />
                  </motion.div>
                </motion.div>
              </motion.div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Animated Polish Names Banner */}
      <section className="border-y border-border bg-accent/20 py-8">
        <div className="overflow-hidden">
          <motion.div
            className="flex gap-8"
            animate={{ x: [0, -1000] }}
            transition={{ duration: 20, repeat: Infinity, ease: "linear" }}
          >
            {[...polishNames, ...polishNames, ...polishNames].map(
              (name, index) => (
                <div
                  key={index}
                  className="flex-shrink-0 text-4xl font-black text-primary opacity-20"
                >
                  {name}
                </div>
              )
            )}
          </motion.div>
        </div>
      </section>

      {/* Features Section with 3D Cards */}
      <section className="py-20">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="mb-16 text-center"
          >
            <h2 className="mb-4 text-4xl font-black text-foreground sm:text-5xl">
              💝 Why You'll Love This Book
            </h2>
            <p className="mx-auto max-w-2xl text-xl text-muted-foreground">
              More than just a coloring book—it's a journey into creativity 🎨,
              culture 🇵🇱, and relaxation 🧘
            </p>
          </motion.div>

          <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
            {features.map((feature, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
                whileHover={{
                  scale: 1.05,
                  rotateY: 10,
                  rotateX: 5,
                  z: 50,
                }}
                style={{ 
                  transformStyle: "preserve-3d",
                  perspective: "1000px"
                }}
              >
                <Card 
                  className="h-full border-2 border-border bg-card shadow-lg transition-all hover:shadow-2xl"
                  style={{ transformStyle: "preserve-3d" }}
                >
                  <CardHeader>
                    <motion.div
                      className="mb-4 flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-primary to-red-700 shadow-lg"
                      whileHover={{ 
                        rotate: 360,
                        scale: 1.2,
                        z: 30,
                        boxShadow: "0 20px 40px rgba(239, 68, 68, 0.4)"
                      }}
                      transition={{ 
                        type: "spring",
                        stiffness: 260,
                        damping: 20
                      }}
                      style={{ 
                        transformStyle: "preserve-3d",
                        transform: "translateZ(20px)"
                      }}
                    >
                      <feature.icon className="h-8 w-8 text-white drop-shadow-md" />
                    </motion.div>
                    <CardTitle className="text-2xl font-bold text-foreground">
                      {feature.title}
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <CardDescription className="text-base leading-relaxed text-muted-foreground">
                      {feature.description}
                    </CardDescription>
                  </CardContent>
                </Card>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* More Sample Images Section */}
      <section className="py-20">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="mb-16 text-center"
          >
            <h2 className="mb-4 text-4xl font-black text-foreground sm:text-5xl">
              🎨 More Beautiful Designs ✨
            </h2>
            <p className="mx-auto max-w-2xl text-xl text-muted-foreground">
              Every page is a unique masterpiece 🖼️ waiting for your creative touch 🌈
            </p>
          </motion.div>

          <div className="grid grid-cols-2 gap-6 md:grid-cols-3 lg:grid-cols-6">
            <motion.div
              initial={{ opacity: 0, y: 20, rotateY: -30 }}
              whileInView={{ opacity: 1, y: 0, rotateY: 0 }}
              viewport={{ once: true }}
              whileHover={{ 
                scale: 1.15, 
                rotateZ: 5,
                z: 50,
                boxShadow: "0 25px 50px rgba(0, 0, 0, 0.3)"
              }}
              transition={{ type: "spring", stiffness: 300, damping: 20 }}
              className="aspect-square overflow-hidden rounded-xl border-2 border-border bg-white shadow-lg cursor-pointer"
              style={{ transformStyle: "preserve-3d" }}
            >
              <img
                src="https://placeholder-image-service.onrender.com/image/300x300?prompt=Bold graffiti style Polish name Anna in thick black outlines with floral decorative elements&id=anna-sample&customer_id=cus_TBW2c0wWSsWpbD"
                alt="Coloring page featuring the Polish name Anna in bold graffiti-style with floral decorative elements and thick outlines"
                className="h-full w-full object-cover"
              />
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 20, rotateY: -30 }}
              whileInView={{ opacity: 1, y: 0, rotateY: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.1, type: "spring", stiffness: 300, damping: 20 }}
              whileHover={{ 
                scale: 1.15, 
                rotateZ: -5,
                z: 50,
                boxShadow: "0 25px 50px rgba(0, 0, 0, 0.3)"
              }}
              className="aspect-square overflow-hidden rounded-xl border-2 border-border bg-white shadow-lg cursor-pointer"
              style={{ transformStyle: "preserve-3d" }}
            >
              <img
                src="https://placeholder-image-service.onrender.com/image/300x300?prompt=Bold graffiti style Polish name Jakub in thick black outlines with geometric patterns&id=jakub-sample&customer_id=cus_TBW2c0wWSsWpbD"
                alt="Coloring page featuring the Polish name Jakub in bold graffiti-style with geometric patterns and thick outlines"
                className="h-full w-full object-cover"
              />
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 20, rotateY: -30 }}
              whileInView={{ opacity: 1, y: 0, rotateY: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.2, type: "spring", stiffness: 300, damping: 20 }}
              whileHover={{ 
                scale: 1.15, 
                rotateZ: 5,
                z: 50,
                boxShadow: "0 25px 50px rgba(0, 0, 0, 0.3)"
              }}
              className="aspect-square overflow-hidden rounded-xl border-2 border-border bg-white shadow-lg cursor-pointer"
              style={{ transformStyle: "preserve-3d" }}
            >
              <img
                src="https://placeholder-image-service.onrender.com/image/300x300?prompt=Bold graffiti style Polish name Katarzyna in thick black outlines with swirls and stars&id=katarzyna-sample&customer_id=cus_TBW2c0wWSsWpbD"
                alt="Coloring page featuring the Polish name Katarzyna in bold graffiti-style with swirls and stars and thick outlines"
                className="h-full w-full object-cover"
              />
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 20, rotateY: -30 }}
              whileInView={{ opacity: 1, y: 0, rotateY: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.3, type: "spring", stiffness: 300, damping: 20 }}
              whileHover={{ 
                scale: 1.15, 
                rotateZ: -5,
                z: 50,
                boxShadow: "0 25px 50px rgba(0, 0, 0, 0.3)"
              }}
              className="aspect-square overflow-hidden rounded-xl border-2 border-border bg-white shadow-lg cursor-pointer"
              style={{ transformStyle: "preserve-3d" }}
            >
              <img
                src="https://placeholder-image-service.onrender.com/image/300x300?prompt=Bold graffiti style Polish name Michał in thick black outlines with urban street art elements&id=michal-sample&customer_id=cus_TBW2c0wWSsWpbD"
                alt="Coloring page featuring the Polish name Michał in bold graffiti-style with urban street art elements and thick outlines"
                className="h-full w-full object-cover"
              />
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 20, rotateY: -30 }}
              whileInView={{ opacity: 1, y: 0, rotateY: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.4, type: "spring", stiffness: 300, damping: 20 }}
              whileHover={{ 
                scale: 1.15, 
                rotateZ: 5,
                z: 50,
                boxShadow: "0 25px 50px rgba(0, 0, 0, 0.3)"
              }}
              className="aspect-square overflow-hidden rounded-xl border-2 border-border bg-white shadow-lg cursor-pointer"
              style={{ transformStyle: "preserve-3d" }}
            >
              <img
                src="https://placeholder-image-service.onrender.com/image/300x300?prompt=Bold graffiti style Polish name Aleksandra in thick black outlines with heart and flower decorations&id=aleksandra-sample&customer_id=cus_TBW2c0wWSsWpbD"
                alt="Coloring page featuring the Polish name Aleksandra in bold graffiti-style with heart and flower decorations and thick outlines"
                className="h-full w-full object-cover"
              />
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 20, rotateY: -30 }}
              whileInView={{ opacity: 1, y: 0, rotateY: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.5, type: "spring", stiffness: 300, damping: 20 }}
              whileHover={{ 
                scale: 1.15, 
                rotateZ: -5,
                z: 50,
                boxShadow: "0 25px 50px rgba(0, 0, 0, 0.3)"
              }}
              className="aspect-square overflow-hidden rounded-xl border-2 border-border bg-white shadow-lg cursor-pointer"
              style={{ transformStyle: "preserve-3d" }}
            >
              <img
                src="https://placeholder-image-service.onrender.com/image/300x300?prompt=Bold graffiti style Polish name Wojciech in thick black outlines with abstract artistic patterns&id=wojciech-sample&customer_id=cus_TBW2c0wWSsWpbD"
                alt="Coloring page featuring the Polish name Wojciech in bold graffiti-style with abstract artistic patterns and thick outlines"
                className="h-full w-full object-cover"
              />
            </motion.div>
          </div>
        </div>
      </section>

      {/* Sample Pages Gallery */}
      <section className="bg-accent/10 py-20">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="mb-16 text-center"
          >
            <h2 className="mb-4 text-4xl font-black text-foreground sm:text-5xl">
              📖 Peek Inside The Book ✨
            </h2>
            <p className="mx-auto max-w-2xl text-xl text-muted-foreground">
              Bold designs 🎨 that bring Polish names to life in stunning graffiti
              style 🖌️
            </p>
          </motion.div>

          <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
            <motion.div
              initial={{ opacity: 0, scale: 0.9, rotateY: -20 }}
              whileInView={{ opacity: 1, scale: 1, rotateY: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.1, type: "spring", stiffness: 200, damping: 20 }}
              whileHover={{ 
                scale: 1.08, 
                rotateZ: 3,
                rotateY: 10,
                z: 40,
                boxShadow: "0 30px 60px rgba(0, 0, 0, 0.25)"
              }}
              style={{ transformStyle: "preserve-3d" }}
            >
              <Card className="overflow-hidden border-2 border-border bg-white shadow-xl cursor-pointer">
                <div className="aspect-square bg-gradient-to-br from-red-50 to-white p-8">
                  <img
                    src="https://placeholder-image-service.onrender.com/image/400x400?prompt=Bold graffiti style Polish name Zofia in thick black outlines with decorative elements suitable for coloring book page&id=zofia-sample&customer_id=cus_TBW2c0wWSsWpbD"
                    alt="Sample coloring page featuring the Polish name Zofia in bold graffiti-style lettering with thick black outlines and decorative flourishes"
                    className="h-full w-full object-contain"
                  />
                </div>
              </Card>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ delay: 0.2 }}
              whileHover={{ scale: 1.05, rotateZ: -3 }}
            >
              <Card className="overflow-hidden border-2 border-border bg-white shadow-xl">
                <div className="aspect-square bg-gradient-to-br from-red-50 to-white p-8">
                  <img
                    src="https://placeholder-image-service.onrender.com/image/400x400?prompt=Bold graffiti style Polish name Jan in thick black outlines with urban art elements suitable for coloring book page&id=jan-sample&customer_id=cus_TBW2c0wWSsWpbD"
                    alt="Sample coloring page featuring the Polish name Jan in bold graffiti-style lettering with thick black outlines and urban art accents"
                    className="h-full w-full object-contain"
                  />
                </div>
              </Card>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ delay: 0.3 }}
              whileHover={{ scale: 1.05, rotateZ: 3 }}
            >
              <Card className="overflow-hidden border-2 border-border bg-white shadow-xl">
                <div className="aspect-square bg-gradient-to-br from-red-50 to-white p-8">
                  <img
                    src="https://placeholder-image-service.onrender.com/image/400x400?prompt=Bold graffiti style Polish name Maria in thick black outlines with artistic patterns suitable for coloring book page&id=maria-sample&customer_id=cus_TBW2c0wWSsWpbD"
                    alt="Sample coloring page featuring the Polish name Maria in bold graffiti-style lettering with thick black outlines and artistic decorative patterns"
                    className="h-full w-full object-contain"
                  />
                </div>
              </Card>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ delay: 0.4 }}
              whileHover={{ scale: 1.05, rotateZ: -3 }}
            >
              <Card className="overflow-hidden border-2 border-border bg-white shadow-xl">
                <div className="aspect-square bg-gradient-to-br from-red-50 to-white p-8">
                  <img
                    src="https://placeholder-image-service.onrender.com/image/400x400?prompt=Bold graffiti style Polish name Piotr in thick black outlines with creative designs suitable for coloring book page&id=piotr-sample&customer_id=cus_TBW2c0wWSsWpbD"
                    alt="Sample coloring page featuring the Polish name Piotr in bold graffiti-style lettering with thick black outlines and creative design elements"
                    className="h-full w-full object-contain"
                  />
                </div>
              </Card>
            </motion.div>
          </div>

          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="mt-12 text-center"
          >
            <Button
              size="lg"
              className="bg-gradient-to-r from-red-600 to-red-700 text-lg font-bold text-white shadow-lg transition-all hover:scale-105"
              onClick={() => window.open('https://www.amazon.com/Stress-Relief-Featuring-Relaxation-Creativity/dp/B0F475VKY9', '_blank')}
            >
              <Book className="mr-2 h-5 w-5" />
              View All 45 Pages on Amazon
            </Button>
          </motion.div>
        </div>
      </section>

      {/* Benefits Grid */}
      <section className="py-20">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 gap-12 lg:grid-cols-2">
            <motion.div
              initial={{ opacity: 0, x: -50 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
            >
              <h2 className="mb-6 text-4xl font-black text-foreground">
                ⭐ What Makes This Book Special?
              </h2>
              <p className="mb-8 text-xl text-muted-foreground">
                Every detail designed with your experience in mind 💖
              </p>

              <div className="space-y-4">
                {benefits.map((benefit, index) => (
                  <motion.div
                    key={index}
                    initial={{ opacity: 0, x: -20 }}
                    whileInView={{ opacity: 1, x: 0 }}
                    viewport={{ once: true }}
                    transition={{ delay: index * 0.1 }}
                    className="flex items-center gap-4 rounded-lg border border-border bg-card p-4 shadow-sm transition-all hover:shadow-md"
                  >
                    <div className="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full bg-primary/10">
                      <Check className="h-5 w-5 text-primary" />
                    </div>
                    <span className="text-lg font-semibold text-foreground">
                      {benefit}
                    </span>
                  </motion.div>
                ))}
              </div>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, x: 50 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              className="relative"
            >
              <Card className="border-2 border-primary/20 bg-gradient-to-br from-primary/5 to-accent/10 p-8 shadow-2xl">
                <div className="mb-6 text-center">
                  <motion.div 
                    className="mb-4 text-6xl font-black text-primary"
                    animate={{ scale: [1, 1.05, 1] }}
                    transition={{ duration: 2, repeat: Infinity }}
                  >
                    💰 $6.99
                  </motion.div>
                  <p className="text-xl font-semibold text-red-600">
                    🔥 Limited Time Offer! ⏰
                  </p>
                </div>

                <div className="space-y-4">
                  <div className="rounded-lg bg-background p-4">
                    <div className="mb-2 flex items-center justify-between">
                      <span className="font-semibold text-foreground">
                        Book Price
                      </span>
                      <span className="text-foreground">$6.99</span>
                    </div>
                    <div className="mb-2 flex items-center justify-between">
                      <span className="font-semibold text-foreground">
                        Shipping to Poland
                      </span>
                      <span className="text-foreground">$11.70</span>
                    </div>
                    <div className="border-t border-border pt-2">
                      <div className="flex items-center justify-between">
                        <span className="text-lg font-bold text-foreground">
                          Total
                        </span>
                        <span className="text-lg font-bold text-primary">
                          $18.69
                        </span>
                      </div>
                    </div>
                  </div>

                  <Button
                    size="lg"
                    className="w-full bg-gradient-to-r from-red-600 to-red-700 text-lg font-bold text-white shadow-lg transition-all hover:scale-105"
                    onClick={() => window.open('https://www.amazon.com/Stress-Relief-Featuring-Relaxation-Creativity/dp/B0F475VKY9', '_blank')}
                  >
                    <ShoppingCart className="mr-2 h-5 w-5" />
                    Order Now on Amazon
                  </Button>

                  <div className="flex items-center justify-center gap-4 text-sm text-muted-foreground">
                    <Award className="h-4 w-4" />
                    <span>30-Day Money-Back Guarantee</span>
                  </div>
                </div>
              </Card>

              {/* Floating Stats */}
              <motion.div
                className="absolute -left-8 top-20 rounded-xl border-2 border-border bg-card p-4 shadow-xl cursor-pointer"
                animate={{ 
                  y: [0, -10, 0],
                  rotateZ: [-2, 2, -2]
                }}
                whileHover={{ 
                  scale: 1.15,
                  rotateY: 15,
                  z: 50,
                  boxShadow: "0 20px 40px rgba(0, 0, 0, 0.3)"
                }}
                transition={{ 
                  y: { duration: 3, repeat: Infinity },
                  rotateZ: { duration: 4, repeat: Infinity }
                }}
                style={{ transformStyle: "preserve-3d" }}
              >
                <motion.div 
                  className="text-3xl font-black text-primary"
                  style={{ transform: "translateZ(20px)" }}
                >
                  45
                </motion.div>
                <div className="text-sm text-muted-foreground">Pages</div>
              </motion.div>

              <motion.div
                className="absolute -right-8 bottom-20 rounded-xl border-2 border-border bg-card p-4 shadow-xl cursor-pointer"
                animate={{ 
                  y: [0, 10, 0],
                  rotateZ: [2, -2, 2]
                }}
                whileHover={{ 
                  scale: 1.15,
                  rotateY: -15,
                  z: 50,
                  boxShadow: "0 20px 40px rgba(0, 0, 0, 0.3)"
                }}
                transition={{ 
                  y: { duration: 3, repeat: Infinity, delay: 0.5 },
                  rotateZ: { duration: 4, repeat: Infinity, delay: 0.5 }
                }}
                style={{ transformStyle: "preserve-3d" }}
              >
                <motion.div 
                  className="text-3xl font-black text-primary"
                  style={{ transform: "translateZ(20px)" }}
                >
                  3-18
                </motion.div>
                <div className="text-sm text-muted-foreground">Age Range</div>
              </motion.div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="bg-accent/10 py-20">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="mb-16 text-center"
          >
            <h2 className="mb-4 text-4xl font-black text-foreground sm:text-5xl">
              💬 What Our Customers Say
            </h2>
            <p className="mx-auto max-w-2xl text-xl text-muted-foreground">
              Join thousands of happy colorists worldwide 🌍✨
            </p>
          </motion.div>

          <div className="grid grid-cols-1 gap-8 md:grid-cols-3">
            {testimonials.map((testimonial, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
                whileHover={{ 
                  scale: 1.08, 
                  rotateZ: 2,
                  rotateY: 5,
                  z: 30,
                  boxShadow: "0 20px 40px rgba(0, 0, 0, 0.2)"
                }}
                style={{ transformStyle: "preserve-3d" }}
              >
                <Card 
                  className="h-full border-2 border-border bg-card shadow-lg transition-all cursor-pointer"
                  style={{ transformStyle: "preserve-3d" }}
                >
                  <CardContent className="p-8">
                    <div className="mb-4 flex items-center justify-center">
                      {[...Array(testimonial.rating)].map((_, i) => (
                        <Star
                          key={i}
                          className="h-6 w-6 fill-yellow-400 text-yellow-400"
                        />
                      ))}
                    </div>
                    <blockquote className="mb-6 text-center text-lg leading-relaxed text-foreground">
                      "{testimonial.text}"
                    </blockquote>
                    <div className="border-t border-border pt-4 text-center">
                      <div className="font-bold text-foreground">
                        {testimonial.name}
                      </div>
                      <div className="text-sm text-muted-foreground">
                        Verified Customer
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Perfect Gift Section */}
      <section className="py-20">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            className="relative overflow-hidden rounded-3xl border-2 border-primary/20 bg-gradient-to-br from-primary/10 via-accent/10 to-background p-12 shadow-2xl"
          >
            <div className="relative z-10 grid grid-cols-1 gap-12 lg:grid-cols-2">
              <div>
                <h2 className="mb-6 text-4xl font-black text-foreground">
                  🎁 The Perfect Gift for Everyone
                </h2>
                <p className="mb-8 text-xl text-muted-foreground">
                  Thoughtful 💝, personalized ✨, and loved by all ages 👨‍👩‍👧‍👦
                </p>

                <div className="space-y-6">
                  <div className="flex items-start gap-4">
                    <Gift className="h-8 w-8 flex-shrink-0 text-primary" />
                    <div>
                      <h3 className="mb-2 text-xl font-bold text-foreground">
                        🎂 Birthday Celebrations
                      </h3>
                      <p className="text-muted-foreground">
                        A unique gift 🎁 that celebrates their name and Polish
                        heritage 🇵🇱
                      </p>
                    </div>
                  </div>

                  <div className="flex items-start gap-4">
                    <Users className="h-8 w-8 flex-shrink-0 text-primary" />
                    <div>
                      <h3 className="mb-2 text-xl font-bold text-foreground">
                        👨‍👩‍👧‍👦 Family Bonding
                      </h3>
                      <p className="text-muted-foreground">
                        Perfect activity for quality time together 💕 while
                        learning Polish names 📚
                      </p>
                    </div>
                  </div>

                  <div className="flex items-start gap-4">
                    <Globe className="h-8 w-8 flex-shrink-0 text-primary" />
                    <div>
                      <h3 className="mb-2 text-xl font-bold text-foreground">
                        📚 Cultural Education
                      </h3>
                      <p className="text-muted-foreground">
                        Ideal for Polish language learners 🗣️ and culture
                        enthusiasts 🌍
                      </p>
                    </div>
                  </div>
                </div>
              </div>

              <div className="flex items-center justify-center">
                <motion.div
                  animate={{ 
                    rotateY: [0, 360],
                    y: [0, -20, 0]
                  }}
                  transition={{ 
                    rotateY: { duration: 20, repeat: Infinity, ease: "linear" },
                    y: { duration: 4, repeat: Infinity, ease: "easeInOut" }
                  }}
                  className="relative"
                >
                  <div className="h-80 w-64 rounded-2xl bg-gradient-to-br from-red-500 to-red-700 p-1 shadow-2xl">
                    <div className="flex h-full w-full flex-col items-center justify-center rounded-xl bg-white p-8 text-center">
                      <motion.div
                        animate={{ scale: [1, 1.1, 1] }}
                        transition={{ duration: 2, repeat: Infinity }}
                      >
                        <Gift className="mb-4 h-20 w-20 text-red-600" />
                      </motion.div>
                      <h3 className="mb-2 text-2xl font-black text-gray-800">
                        🎁 Gift Ready ✨
                      </h3>
                      <p className="text-gray-600">
                        Beautiful packaging 📦 perfect for any occasion 🎉
                      </p>
                    </div>
                  </div>
                  
                  {/* Sparkle effects */}
                  <motion.div
                    className="absolute -right-4 top-12"
                    animate={{ 
                      scale: [0, 1, 0],
                      rotate: [0, 180, 360]
                    }}
                    transition={{ duration: 2, repeat: Infinity, delay: 0 }}
                  >
                    <Sparkles className="h-8 w-8 text-yellow-400" />
                  </motion.div>
                  
                  <motion.div
                    className="absolute -left-4 bottom-12"
                    animate={{ 
                      scale: [0, 1, 0],
                      rotate: [360, 180, 0]
                    }}
                    transition={{ duration: 2, repeat: Infinity, delay: 1 }}
                  >
                    <Sparkles className="h-6 w-6 text-yellow-400" />
                  </motion.div>
                </motion.div>
              </div>
            </div>

            {/* Background Decoration */}
            <div className="absolute -right-20 -top-20 h-64 w-64 rounded-full bg-primary/10 blur-3xl" />
            <div className="absolute -bottom-20 -left-20 h-64 w-64 rounded-full bg-accent/10 blur-3xl" />
          </motion.div>
        </div>
      </section>

      {/* Final CTA Section */}
      <section className="relative overflow-hidden bg-gradient-to-br from-red-600 to-red-800 py-20 text-white">
        <div className="container relative z-10 mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="mx-auto max-w-4xl text-center"
          >
            <h2 className="mb-6 text-4xl font-black sm:text-5xl lg:text-6xl">
              🎨 Ready to Start Coloring Your Way to Calm? 🧘✨
            </h2>
            <p className="mb-8 text-xl opacity-90">
              Join thousands of happy customers 😊 and transform stress into
              creativity today! 🌈💫
            </p>

            <div className="mb-8 flex flex-col items-center justify-center gap-4 sm:flex-row">
              <Button
                size="lg"
                className="group bg-white text-xl font-bold text-red-700 shadow-xl transition-all hover:scale-110 hover:bg-gray-100"
                onClick={() => window.open('https://www.amazon.com/Stress-Relief-Featuring-Relaxation-Creativity/dp/B0F475VKY9', '_blank')}
              >
                <ShoppingCart className="mr-2 h-6 w-6" />
                Get Your Copy Now - $6.99
                <ChevronRight className="ml-2 h-6 w-6 transition-transform group-hover:translate-x-2" />
              </Button>
            </div>

            <div className="flex flex-wrap items-center justify-center gap-6 text-sm opacity-90">
              <div className="flex items-center gap-2">
                <Check className="h-5 w-5" />
                <span>⚡ Ships within 22 hours</span>
              </div>
              <div className="flex items-center gap-2">
                <Check className="h-5 w-5" />
                <span>💯 30-Day Money-Back Guarantee</span>
              </div>
              <div className="flex items-center gap-2">
                <Check className="h-5 w-5" />
                <span>🔐 Secure Amazon Checkout</span>
              </div>
            </div>
          </motion.div>
        </div>

        {/* Animated Background Pattern */}
        <div className="absolute inset-0 opacity-10">
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(255,255,255,0.1),transparent_50%)]" />
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-border bg-card py-12">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 gap-8 md:grid-cols-3">
            <div>
              <h3 className="mb-4 text-2xl font-black text-primary">
                🇵🇱 Polish Names Coloring Book 🎨
              </h3>
              <p className="mb-4 text-sm text-muted-foreground">
                Transform stress into creativity ✨ with 45 hand-drawn pages 📖 of
                beautiful Polish names in graffiti style 🖌️.
              </p>
              <div className="flex items-center gap-1">
                {[...Array(5)].map((_, i) => (
                  <Star
                    key={i}
                    className="h-4 w-4 fill-yellow-400 text-yellow-400"
                  />
                ))}
                <span className="ml-2 text-sm font-semibold text-foreground">
                  5.0 Rating
                </span>
              </div>
            </div>

            <div>
              <h4 className="mb-4 font-bold text-foreground">
                Product Details
              </h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li>Publisher: Independently Published</li>
                <li>Publication Date: April 5, 2025</li>
                <li>Language: English</li>
                <li>Pages: 46</li>
                <li>Dimensions: 8.5 x 0.11 x 8.5 inches</li>
                <li>ISBN-13: 979-8316957521</li>
              </ul>
            </div>

            <div>
              <h4 className="mb-4 font-bold text-foreground">Author</h4>
              <p className="mb-4 text-sm text-muted-foreground">
                By Mr Dhiya Eddine Akram Khelaifia
              </p>
              <p className="text-sm text-muted-foreground">
                Book 1 of the Polish Names Stress Relief Coloring Book Series
              </p>
              <div className="mt-6">
                <Button
                  variant="outline"
                  className="w-full border-primary text-primary hover:bg-primary hover:text-white"
                  onClick={() => window.open('https://www.amazon.com/Stress-Relief-Featuring-Relaxation-Creativity/dp/B0F475VKY9', '_blank')}
                >
                  View on Amazon
                </Button>
              </div>
            </div>
          </div>

          <div className="mt-8 flex flex-col items-center justify-between border-t border-border pt-8 sm:flex-row">
            <p className="text-sm text-muted-foreground">
              © 2025 Polish Names Coloring Book. All rights reserved.
            </p>
            <div className="mt-4 flex gap-6 sm:mt-0">
              <a
                href="#"
                className="text-sm text-muted-foreground transition-colors hover:text-primary"
              >
                Privacy Policy
              </a>
              <a
                href="#"
                className="text-sm text-muted-foreground transition-colors hover:text-primary"
              >
                Terms of Service
              </a>
              <a
                href="#"
                className="text-sm text-muted-foreground transition-colors hover:text-primary"
              >
                Contact
              </a>
            </div>
          </div>
        </div>
      </footer>
    </main>
  );
}
