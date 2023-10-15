using System;

public class Kata
{
  public static int Litres(double time)
  {
    // Nathan drinks 0.5 liters of water per hour
    double litres = 0.5 * time;

    // Round down to the nearest whole number
    int roundedLitres = (int)Math.Floor(litres);

    return roundedLitres;
  }
}