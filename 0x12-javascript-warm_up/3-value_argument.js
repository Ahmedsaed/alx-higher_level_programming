#!/usr/bin/node
import { argv } from 'node:process';

if (argv) {
  console.log('No argument');
} else {
  console.log(argv[1]);
}
