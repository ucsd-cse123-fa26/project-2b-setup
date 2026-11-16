# Project 2b Setup

Project 2b builds on your Project 2a router, so keep working in your Project 2a repo. This repo contains the new lab environment (a network with four routers), the updated test harness and the routing tables. Your `sr_*.c` files are not changed.

## Apply the update

Open your Project 2a codespace. In its terminal, at the top level of your repo, paste:

```bash
git add -A; git commit -m "PA2a final"  # commits all the changes you've made in your codespace so far
git clone https://github.com/ucsd-cse123-fa26/project-2b-setup /tmp/pa2b && \
rm -rf tests rtables .devcontainer/project-base && \
cp -r /tmp/pa2b/.devcontainer/project-base .devcontainer/ && \
cp -r /tmp/pa2b/tests /tmp/pa2b/rtables /tmp/pa2b/.vscode /tmp/pa2b/rtable* .
git add -A && git commit -m "PA2b setup" && git push
```

## Rebuild the container

Press **Ctrl+Shift+P** (**Cmd+Shift+P** on Mac) and run
**Codespaces: Rebuild Container**. Once the container has been rebuilt, your lab environment should be updated and you're ready to start working on Project 2b.

## Check that the rebuild worked

In the rebuilt codespace, run:

```bash
cat /project-base/IP_CONFIG
```

You should see entries for `sw1` through `sw4`. If you don't, make sure you pushed your changes from the first step (`git push`), then rebuild the container again.

## Running the lab

You can either press **Ctrl+Shift+B** (**Cmd+Shift+B** on Mac) and choose **Create PA2b terminals**, or follow the instructions in the Project 2b spec.
